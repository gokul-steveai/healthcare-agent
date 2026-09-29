param(
    [string]$DataPath = '/home/ayush/Downloads/synthea_sample_data_csv_apr2020/csv',
    [string]$OutputPath = (Join-Path $PSScriptRoot 'hero_patient_selection.md')
)

$ErrorActionPreference = 'Stop'
$requiredFiles = @('patients', 'conditions', 'medications', 'observations', 'encounters')
$data = @{}
foreach ($name in $requiredFiles) {
    $path = Join-Path $DataPath ($name + '.csv')
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Required file not found: $path"
    }
    $data[$name] = @(Import-Csv -LiteralPath $path)
}

function Get-CountsByPatient {
    param([object[]]$Rows)
    $result = @{}
    $Rows | Group-Object PATIENT | ForEach-Object { $result[$_.Name] = $_.Count }
    return $result
}

function Get-TopDescriptions {
    param([object[]]$Rows, [int]$Limit = 6)
    $items = @(
        $Rows |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_.DESCRIPTION) } |
            Group-Object DESCRIPTION |
            Sort-Object @{ Expression = 'Count'; Descending = $true }, Name |
            Select-Object -First $Limit
    )
    return (($items | ForEach-Object { "$($_.Name) ($($_.Count))" }) -join '; ')
}

function Get-KeyConditions {
    param([object[]]$Rows, [int]$Limit = 8)
    $groups = @(
        $Rows |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_.DESCRIPTION) } |
            Group-Object DESCRIPTION
    )
    $selected = [System.Collections.Generic.List[object]]::new()
    foreach ($requiredDiagnosis in @('Diabetes', 'Hypertension')) {
        $match = $groups | Where-Object { $_.Name -ieq $requiredDiagnosis } | Select-Object -First 1
        if ($null -ne $match) { $selected.Add($match) }
    }
    $groups |
        Where-Object { $_.Name -ine 'Diabetes' -and $_.Name -ine 'Hypertension' } |
        Sort-Object @{ Expression = 'Count'; Descending = $true }, Name |
        Select-Object -First ($Limit - $selected.Count) |
        ForEach-Object { $selected.Add($_) }
    return (($selected | ForEach-Object { "$($_.Name) ($($_.Count))" }) -join '; ')
}

function Get-PercentileMap {
    param([object[]]$Rows, [string]$Property)
    $ordered = @($Rows | Sort-Object $Property, PatientID)
    $map = @{}
    if ($ordered.Count -eq 1) {
        $map[$ordered[0].PatientID] = 1.0
        return $map
    }
    for ($index = 0; $index -lt $ordered.Count; $index++) {
        $map[$ordered[$index].PatientID] = $index / ($ordered.Count - 1)
    }
    return $map
}

function Get-MarkdownTable {
    param([object[]]$Rows, [string[]]$Properties, [string[]]$Headers)
    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add('| ' + ($Headers -join ' | ') + ' |')
    $lines.Add('| ' + (($Headers | ForEach-Object { '---' }) -join ' | ') + ' |')
    foreach ($row in $Rows) {
        $values = foreach ($property in $Properties) {
            ([string]$row.$property).Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
        }
        $lines.Add('| ' + ($values -join ' | ') + ' |')
    }
    return $lines
}

$diabetesPatients = @(
    $data.conditions |
        Where-Object { $_.DESCRIPTION.Trim() -ieq 'Diabetes' } |
        Select-Object -ExpandProperty PATIENT -Unique
)
$hypertensionPatients = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$data.conditions |
    Where-Object { $_.DESCRIPTION.Trim() -ieq 'Hypertension' } |
    ForEach-Object { [void]$hypertensionPatients.Add($_.PATIENT) }
$cohortIds = @($diabetesPatients | Where-Object { $hypertensionPatients.Contains($_) })

$patientMap = @{}
$data.patients | ForEach-Object { $patientMap[$_.Id] = $_ }
$conditionCounts = Get-CountsByPatient $data.conditions
$medicationCounts = Get-CountsByPatient $data.medications
$observationCounts = Get-CountsByPatient $data.observations
$encountersByPatient = @{}
$data.encounters | Group-Object PATIENT | ForEach-Object { $encountersByPatient[$_.Name] = @($_.Group) }

$eligible = @(
    foreach ($patientId in $cohortIds) {
        $encounters = @($encountersByPatient[$patientId])
        $encounterDates = @($encounters | ForEach-Object { [datetimeoffset]::Parse($_.START) } | Sort-Object)
        if ($encounterDates.Count -lt 2) { continue }
        $firstEncounter = $encounterDates[0]
        $lastEncounter = $encounterDates[-1]
        $spanDays = [int][math]::Floor(($lastEncounter - $firstEncounter).TotalDays)
        $conditions = [int]$conditionCounts[$patientId]
        $medications = [int]$medicationCounts[$patientId]
        $observations = [int]$observationCounts[$patientId]
        if ($conditions -lt 10 -or $medications -lt 20 -or $observations -lt 200 -or $spanDays -le 0) { continue }

        $patient = $patientMap[$patientId]
        $birthdate = [datetime]::ParseExact($patient.BIRTHDATE, 'yyyy-MM-dd', $null)
        $lastDate = $lastEncounter.UtcDateTime.Date
        $age = $lastDate.Year - $birthdate.Year
        if ($birthdate.Date -gt $lastDate.AddYears(-$age)) { $age-- }

        [pscustomobject]@{
            PatientID = $patientId
            Age = $age
            Gender = $patient.GENDER
            Conditions = $conditions
            Medications = $medications
            Observations = $observations
            Encounters = $encounters.Count
            SpanDays = $spanDays
            FirstEncounter = $firstEncounter.ToString('yyyy-MM-dd')
            LastEncounter = $lastEncounter.ToString('yyyy-MM-dd')
        }
    }
)

$metrics = @('Conditions', 'Medications', 'Observations', 'Encounters', 'SpanDays')
$percentiles = @{}
foreach ($metric in $metrics) { $percentiles[$metric] = Get-PercentileMap $eligible $metric }
foreach ($candidate in $eligible) {
    $sum = 0.0
    foreach ($metric in $metrics) { $sum += $percentiles[$metric][$candidate.PatientID] }
    $candidate | Add-Member -NotePropertyName RichnessScore -NotePropertyValue ([math]::Round(100 * $sum / $metrics.Count, 1))
}

$topFive = @(
    $eligible |
        Sort-Object @{ Expression = 'RichnessScore'; Descending = $true }, @{ Expression = 'Conditions'; Descending = $true }, PatientID |
        Select-Object -First 5 |
        ForEach-Object {
            $patientId = $_.PatientID
            $conditions = @($data.conditions | Where-Object { $_.PATIENT -eq $patientId })
            $medications = @($data.medications | Where-Object { $_.PATIENT -eq $patientId })
            $observations = @($data.observations | Where-Object { $_.PATIENT -eq $patientId })
            [pscustomobject]@{
                PatientID = $patientId
                Age = $_.Age
                Gender = $_.Gender
                Conditions = $_.Conditions
                Medications = $_.Medications
                Observations = $_.Observations
                FirstEncounter = $_.FirstEncounter
                LastEncounter = $_.LastEncounter
                KeyConditions = Get-KeyConditions $conditions
                KeyMedications = Get-TopDescriptions $medications
                KeyLabTypes = Get-TopDescriptions $observations
                RichnessScore = $_.RichnessScore
                Encounters = $_.Encounters
            }
        }
)

$report = [System.Collections.Generic.List[string]]::new()
$report.Add('# Hero Patient Selection')
$report.Add('')
$report.Add("- Source directory: ``$DataPath``")
$report.Add(('- Starting cohort: **{0}** patients with exact condition descriptions `Diabetes` and `Hypertension`.' -f $cohortIds.Count))
$report.Add("- Eligible after thresholds and longitudinal-history requirement: **$($eligible.Count)** patients.")
$report.Add('- Required thresholds: at least 10 condition rows, 20 medication rows, 200 observation rows, two encounters, and a positive encounter timespan.')
$report.Add('- Ranking: equal-weight average percentile across condition rows, medication rows, observation rows, encounter count, and encounter timespan. This score is used only for deterministic dataset selection.')
$report.Add("- Age is calculated on the patient's last encounter date. Totals count CSV rows; key conditions include the cohort-defining diagnoses plus other frequent conditions, and other key items show the six most frequent descriptions. Frequencies appear in parentheses.")
$report.Add('- "Key Lab Types" uses `observations.DESCRIPTION`; Synthea stores both laboratory tests and clinical measurements in that field.')
$report.Add('')
$report.Add('## Selected Top 5')
$report.Add('')
$summaryRows = $topFive | Select-Object PatientID, Age, Gender, Conditions, Medications, Observations, FirstEncounter, LastEncounter
$report.AddRange([string[]](Get-MarkdownTable $summaryRows @('PatientID', 'Age', 'Gender', 'Conditions', 'Medications', 'Observations', 'FirstEncounter', 'LastEncounter') @('Patient ID', 'Age', 'Gender', 'Total Conditions', 'Total Medications', 'Total Observations', 'First Encounter Date', 'Last Encounter Date')))
$report.Add('')

$rank = 1
foreach ($hero in $topFive) {
    $report.Add("## $rank. $($hero.PatientID)")
    $report.Add('')
    $report.Add("- Age / gender: **$($hero.Age) / $($hero.Gender)**")
    $report.Add("- Clinical totals: **$($hero.Conditions)** conditions, **$($hero.Medications)** medications, **$($hero.Observations)** observations")
    $report.Add("- Longitudinal history: **$($hero.Encounters)** encounters from **$($hero.FirstEncounter)** to **$($hero.LastEncounter)**")
    $report.Add("- Selection richness score: **$($hero.RichnessScore)** / 100")
    $report.Add("- Key conditions: $($hero.KeyConditions)")
    $report.Add("- Key medications: $($hero.KeyMedications)")
    $report.Add("- Key lab/observation types: $($hero.KeyLabTypes)")
    $report.Add('')
    $rank++
}

$report | Set-Content -LiteralPath $OutputPath -Encoding utf8
Write-Output "Created $OutputPath with $($topFive.Count) selected patients from $($eligible.Count) eligible patients."
