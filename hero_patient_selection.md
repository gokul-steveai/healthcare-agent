# Hero Patient Selection

- Source directory: `/home/ayush/Downloads/synthea_sample_data_csv_apr2020/csv`
- Starting cohort: **44** patients with exact condition descriptions `Diabetes` and `Hypertension`.
- Eligible after thresholds and longitudinal-history requirement: **36** patients.
- Required thresholds: at least 10 condition rows, 20 medication rows, 200 observation rows, two encounters, and a positive encounter timespan.
- Ranking: equal-weight average percentile across condition rows, medication rows, observation rows, encounter count, and encounter timespan. This score is used only for deterministic dataset selection.
- Age is calculated on the patient's last encounter date. Totals count CSV rows; key conditions include the cohort-defining diagnoses plus other frequent conditions, and other key items show the six most frequent descriptions. Frequencies appear in parentheses.
- "Key Lab Types" uses `observations.DESCRIPTION`; Synthea stores both laboratory tests and clinical measurements in that field.

## Selected Top 5

| Patient ID | Age | Gender | Total Conditions | Total Medications | Total Observations | First Encounter Date | Last Encounter Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6ec18ddf-e9ee-421a-9033-456f558c7b4b | 68 | M | 25 | 436 | 2184 | 1943-03-31 | 2005-03-23 |
| 2c71dd97-7085-416a-aa07-d675bbe3adf2 | 79 | F | 21 | 1563 | 1617 | 1947-08-08 | 2020-04-03 |
| 714b9c18-783d-4f52-aa64-cc3a05a286d9 | 74 | M | 21 | 490 | 1567 | 1959-09-30 | 2020-04-01 |
| 3acf9313-1874-4dff-ab2a-3187516d92d6 | 100 | M | 15 | 1237 | 2655 | 1934-06-25 | 2018-01-21 |
| 9c4c1885-35af-48b9-a09f-4ea448d40d75 | 91 | F | 17 | 482 | 827 | 1940-04-09 | 2013-08-20 |

## 1. 6ec18ddf-e9ee-421a-9033-456f558c7b4b

- Age / gender: **68 / M**
- Clinical totals: **25** conditions, **436** medications, **2184** observations
- Longitudinal history: **367** encounters from **1943-03-31** to **2005-03-23**
- Selection richness score: **91.4** / 100
- Key conditions: Diabetes (1); Hypertension (1); Polyp of colon (3); Laceration of hand (2); Viral sinusitis (disorder) (2); Anemia (disorder) (1); Carcinoma in situ of prostate (disorder) (1); Chronic kidney disease stage 1 (disorder) (1)
- Key medications: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet (205); insulin human  isophane 70 UNT/ML / Regular Insulin  Human 30 UNT/ML Injectable Suspension [Humulin] (176); Cisplatin 50 MG Injection (24); PACLitaxel 100 MG Injection (24); 0.25 ML Leuprolide Acetate 30 MG/ML Prefilled Syringe (1); 1 ML DOCEtaxel 20 MG/ML Injection (1)
- Key lab/observation types: Calcium (88); Carbon Dioxide (88); Chloride (88); Creatinine (88); Glucose (88); Potassium (88)

## 2. 2c71dd97-7085-416a-aa07-d675bbe3adf2

- Age / gender: **79 / F**
- Clinical totals: **21** conditions, **1563** medications, **1617** observations
- Longitudinal history: **367** encounters from **1947-08-08** to **2020-04-03**
- Selection richness score: **91.4** / 100
- Key conditions: Diabetes (1); Hypertension (1); Acute bronchitis (disorder) (2); Acute viral pharyngitis (disorder) (1); Anemia (disorder) (1); Atrial Fibrillation (1); Body mass index 30+ - obesity (finding) (1); Body mass index 40+ - severely obese (finding) (1)
- Key medications: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet (258); 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet (248); Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] (232); Digoxin 0.125 MG Oral Tablet (172); Verapamil Hydrochloride 40 MG (172); Warfarin Sodium 5 MG Oral Tablet (172)
- Key lab/observation types: Body Height (65); Body Mass Index (65); Body Weight (65); Calcium (65); Carbon Dioxide (65); Chloride (65)

## 3. 714b9c18-783d-4f52-aa64-cc3a05a286d9

- Age / gender: **74 / M**
- Clinical totals: **21** conditions, **490** medications, **1567** observations
- Longitudinal history: **375** encounters from **1959-09-30** to **2020-04-01**
- Selection richness score: **89.7** / 100
- Key conditions: Diabetes (1); Hypertension (1); Viral sinusitis (disorder) (3); Anemia (disorder) (1); Body mass index 30+ - obesity (finding) (1); Carcinoma in situ of prostate (disorder) (1); Cardiac Arrest (1); Chronic kidney disease stage 1 (disorder) (1)
- Key medications: Hydrochlorothiazide 25 MG Oral Tablet (254); insulin human  isophane 70 UNT/ML / Regular Insulin  Human 30 UNT/ML Injectable Suspension [Humulin] (228); 0.25 ML Leuprolide Acetate 30 MG/ML Prefilled Syringe (1); 1 ML DOCEtaxel 20 MG/ML Injection (1); 10 ML oxaliplatin 5 MG/ML Injection (1); Alendronic acid 10 MG Oral Tablet (1)
- Key lab/observation types: Body Height (63); Body Mass Index (63); Body Weight (63); Calcium (63); Carbon Dioxide (63); Chloride (63)

## 4. 3acf9313-1874-4dff-ab2a-3187516d92d6

- Age / gender: **100 / M**
- Clinical totals: **15** conditions, **1237** medications, **2655** observations
- Longitudinal history: **826** encounters from **1934-06-25** to **2018-01-21**
- Selection richness score: **86.9** / 100
- Key conditions: Diabetes (1); Hypertension (1); Acute bronchitis (disorder) (1); Alcoholism (1); Alzheimer's disease (disorder) (1); Anemia (disorder) (1); Atrial Fibrillation (1); Body mass index 30+ - obesity (finding) (1)
- Key medications: Hydrochlorothiazide 25 MG Oral Tablet (338); insulin human  isophane 70 UNT/ML / Regular Insulin  Human 30 UNT/ML Injectable Suspension [Humulin] (295); Digoxin 0.125 MG Oral Tablet (199); Verapamil Hydrochloride 40 MG (199); Warfarin Sodium 5 MG Oral Tablet (199); 0.25 ML Leuprolide Acetate 30 MG/ML Prefilled Syringe (1)
- Key lab/observation types: Diastolic Blood Pressure (246); Systolic Blood Pressure (246); Calcium (99); Carbon Dioxide (99); Chloride (99); Creatinine (99)

## 5. 9c4c1885-35af-48b9-a09f-4ea448d40d75

- Age / gender: **91 / F**
- Clinical totals: **17** conditions, **482** medications, **827** observations
- Longitudinal history: **144** encounters from **1940-04-09** to **2013-08-20**
- Selection richness score: **80** / 100
- Key conditions: Diabetes (1); Hypertension (1); Acute viral pharyngitis (disorder) (1); Anemia (disorder) (1); Atrial Fibrillation (1); Body mass index 30+ - obesity (finding) (1); Chronic kidney disease stage 1 (disorder) (1); Diabetic renal disease (disorder) (1)
- Key medications: Atenolol 50 MG / Chlorthalidone 25 MG Oral Tablet (123); 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet (97); insulin human  isophane 70 UNT/ML / Regular Insulin  Human 30 UNT/ML Injectable Suspension [Humulin] (65); Digoxin 0.125 MG Oral Tablet (64); Verapamil Hydrochloride 40 MG (64); Warfarin Sodium 5 MG Oral Tablet (64)
- Key lab/observation types: Body Height (33); Body Mass Index (33); Body Weight (33); Calcium (33); Carbon Dioxide (33); Chloride (33)

