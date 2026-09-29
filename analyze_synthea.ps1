param(
    [string]$DataPath = '/home/ayush/Downloads/synthea_sample_data_csv_apr2020/csv',
    [string]$OutputPath = (Join-Path $PSScriptRoot 'synthea_csv_summary.md')
)

$ErrorActionPreference = 'Stop'
$fileNames = @('patients', 'conditions', 'medications', 'observations')
$data = @{}

foreach ($name in $fileNames) {
    $path = Join-Path $DataPath ($name + '.csv')
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Required file not found: $path"
    }
    $data[$name] = @(Import-Csv -LiteralPath $path)
}

function Get-MarkdownTable {
    param([object[]]$Rows, [string[]]$Properties, [string[]]$Headers)

    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add('| ' + ($Headers -join ' | ') + ' |')
    $lines.Add('| ' + (($Headers | ForEach-Object { '---' }) -join ' | ') + ' |')
    foreach ($row in $Rows) {
        $values = foreach ($property in $Properties) {
            $value = [string]$row.$property
            $value.Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
        }
        $lines.Add('| ' + ($values -join ' | ') + ' |')
    }
    return $lines
}

$topConditions = @(
    $data.conditions |
        Group-Object DESCRIPTION |
        Sort-Object @{ Expression = 'Count'; Descending = $true }, Name |
        Select-Object -First 20 @{ Name = 'Description'; Expression = { $_.Name } }, Count
)

$topObservations = @(
    $data.observations |
        Group-Object DESCRIPTION |
        Sort-Object @{ Expression = 'Count'; Descending = $true }, Name |
        Select-Object -First 20 @{ Name = 'Description'; Expression = { $_.Name } }, Count
)

$diabetesIds = @(
    $data.conditions |
        Where-Object { $_.DESCRIPTION.Trim() -ieq 'Diabetes' } |
        Select-Object -ExpandProperty PATIENT -Unique
)
$hypertensionSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$data.conditions |
    Where-Object { $_.DESCRIPTION.Trim() -ieq 'Hypertension' } |
    ForEach-Object { [void]$hypertensionSet.Add($_.PATIENT) }
$bothIds = @($diabetesIds | Where-Object { $hypertensionSet.Contains($_) })

$conditionCounts = @{}
$medicationCounts = @{}
$observationCounts = @{}
$data.conditions | Group-Object PATIENT | ForEach-Object { $conditionCounts[$_.Name] = $_.Count }
$data.medications | Group-Object PATIENT | ForEach-Object { $medicationCounts[$_.Name] = $_.Count }
$data.observations | Group-Object PATIENT | ForEach-Object { $observationCounts[$_.Name] = $_.Count }

$patientMap = @{}
$data.patients | ForEach-Object { $patientMap[$_.Id] = $_ }
$cohort = @(
    $bothIds | ForEach-Object {
        $patient = $patientMap[$_]
        [pscustomobject]@{
            PatientID   = $_
            Gender      = $patient.GENDER
            Birthdate   = $patient.BIRTHDATE
            Conditions  = [int]$conditionCounts[$_]
            Medications = if ($medicationCounts.ContainsKey($_)) { [int]$medicationCounts[$_] } else { 0 }
            Observations = if ($observationCounts.ContainsKey($_)) { [int]$observationCounts[$_] } else { 0 }
        }
    } | Sort-Object PatientID
)

$report = [System.Collections.Generic.List[string]]::new()
$report.Add('# Synthea CSV Dataset Summary')
$report.Add('')
$report.Add("- Source directory: ``$DataPath``")
$report.Add('- Analysis scope: `patients.csv`, `conditions.csv`, `medications.csv`, and `observations.csv`')
$report.Add('- Condition cohort rule: case-insensitive exact matches on `conditions.DESCRIPTION` for `Diabetes` and `Hypertension` for the same patient.')
$report.Add('- Per-patient totals are row counts in each corresponding CSV across the complete dataset; they are not distinct-description counts.')
$report.Add('')
$report.Add('## Record Counts')
$report.Add('')
$recordRows = foreach ($name in $fileNames) {
    [pscustomobject]@{ File = $name + '.csv'; Records = $data[$name].Count }
}
$report.AddRange([string[]](Get-MarkdownTable $recordRows @('File', 'Records') @('File', 'Total records')))
$report.Add('')
$report.Add('## Columns')
$report.Add('')
foreach ($name in $fileNames) {
    $columns = @($data[$name][0].PSObject.Properties.Name)
    $report.Add("### $name.csv")
    $report.Add('')
    $report.Add(($columns | ForEach-Object { "``$_``" }) -join ', ')
    $report.Add('')
}
$report.Add('## Top 20 Conditions by Frequency')
$report.Add('')
$report.AddRange([string[]](Get-MarkdownTable $topConditions @('Description', 'Count') @('Condition', 'Frequency')))
$report.Add('')
$report.Add('## Top 20 Observation Types by Frequency')
$report.Add('')
$report.AddRange([string[]](Get-MarkdownTable $topObservations @('Description', 'Count') @('Observation type (`DESCRIPTION`)', 'Frequency')))
$report.Add('')
$report.Add('## Patients with Both Diabetes and Hypertension')
$report.Add('')
$report.Add("Qualifying patients: **$($cohort.Count)**")
$report.Add('')
$report.AddRange([string[]](Get-MarkdownTable $cohort @('PatientID', 'Gender', 'Birthdate', 'Conditions', 'Medications', 'Observations') @('Patient ID', 'Gender', 'Birthdate', 'Number of conditions', 'Number of medications', 'Number of observations')))
$report.Add('')

$report | Set-Content -LiteralPath $OutputPath -Encoding utf8
Write-Output "Created $OutputPath with $($cohort.Count) qualifying patients."
