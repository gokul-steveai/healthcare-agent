# Complete Patient Timeline

- Patient ID: `2c71dd97-7085-416a-aa07-d675bbe3adf2`
- Birthdate: **1941-02-14**
- Age at last encounter: **79**
- Gender: **F**
- Encounter span: **1947-08-08** to **2020-04-03**
- Source records: **1** patient, **21** conditions, **1563** medication records, **1617** observations, **367** encounters

## Reading the Report

- Events are ordered by source timestamp. A medication row creates a start event and, when `STOP` is present, a medication-change/end event.
- **DIABETES** and **HYPERTENSION** are deterministic keyword matches across descriptions, reasons, measurements, and medication names.
- **SIGNIFICANT CHANGE** means a numeric observation changed by at least 50% from the immediately preceding result of the same type. It is a data-change flag, not a clinical judgment or recommendation.
- Synthea stores laboratory tests and other clinical measurements together in `observations.csv`; all appear under Lab Results.

# A. Full Timeline

| Date/time | Event group | Event | Highlights | Source |
| --- | --- | --- | --- | --- |
| 1947-08-08 00:00:00 | Diagnoses | Cardiac Arrest code=410429000 |  | conditions.csv |
| 1947-08-08 00:00:00 | Diagnoses | History of cardiac arrest (situation) code=429007001 |  | conditions.csv |
| 1947-08-08 20:51:21 | Encounters | Cardiac Arrest; class=emergency; end=1947-08-08T22:36:21Z |  | encounters.csv |
| 1956-03-23 00:00:00 | Diagnoses | Body mass index 30+ - obesity (finding) code=162864005 |  | conditions.csv |
| 1956-03-23 20:51:21 | Encounters | Well child visit (procedure); class=wellness; end=1956-03-23T21:21:21Z |  | encounters.csv |
| 1957-03-29 00:00:00 | Diagnoses | Body mass index 40+ - severely obese (finding) code=408512008 |  | conditions.csv |
| 1957-03-29 20:51:21 | Encounters | Well child visit (procedure); class=wellness; end=1957-03-29T21:21:21Z |  | encounters.csv |
| 1959-04-10 00:00:00 | Diagnoses | Hypertension code=59621000 | **HYPERTENSION** | conditions.csv |
| 1959-04-10 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1959-04-10T21:06:21Z |  | encounters.csv |
| 1959-07-09 20:51:21 | Encounters | Hypertension follow-up encounter; class=ambulatory; end=1959-07-09T21:06:21Z | **HYPERTENSION** | encounters.csv |
| 1959-07-09 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=9; total cost=2371.41 | **HYPERTENSION** | medications.csv |
| 1960-04-15 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1960-04-15T21:21:21Z |  | encounters.csv |
| 1960-04-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1960-04-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1961-04-21 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1961-04-21T21:06:21Z |  | encounters.csv |
| 1961-04-21 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1961-04-21 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1962-04-27 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1962-04-27T21:21:21Z |  | encounters.csv |
| 1962-04-27 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1962-04-27 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1963-05-03 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1963-05-03T21:06:21Z |  | encounters.csv |
| 1963-05-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1963-05-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1964-05-08 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1964-05-08T21:21:21Z |  | encounters.csv |
| 1964-05-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1964-05-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1965-05-14 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1965-05-14T21:06:21Z |  | encounters.csv |
| 1965-05-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1965-05-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1966-05-20 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1966-05-20T21:06:21Z |  | encounters.csv |
| 1966-05-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1966-05-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1967-05-26 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1967-05-26T21:21:21Z |  | encounters.csv |
| 1967-05-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1967-05-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1968-05-31 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1968-05-31T21:21:21Z |  | encounters.csv |
| 1968-05-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1968-05-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1969-06-06 00:00:00 | Diagnoses | Anemia (disorder) code=271737000 |  | conditions.csv |
| 1969-06-06 00:00:00 | Diagnoses | Diabetes code=44054006 | **DIABETES** | conditions.csv |
| 1969-06-06 20:51:21 | Encounters | Encounter for problem; class=ambulatory; reason=Anemia (disorder); end=1969-06-06T22:19:21Z |  | encounters.csv |
| 1969-06-06 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1969-06-06T21:06:21Z |  | encounters.csv |
| 1969-06-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1969-06-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1969-06-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1969-06-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=502.25 | **DIABETES** | medications.csv |
| 1969-06-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=5928.72 | **DIABETES** | medications.csv |
| 1969-06-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1969-06-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1970-06-12 00:00:00 | Diagnoses | Hypertriglyceridemia (disorder) code=302870006 |  | conditions.csv |
| 1970-06-12 00:00:00 | Diagnoses | Metabolic syndrome X (disorder) code=237602007 |  | conditions.csv |
| 1970-06-12 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1970-06-12T21:06:21Z |  | encounters.csv |
| 1970-06-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1970-06-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1970-06-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=2413.80 | **DIABETES** | medications.csv |
| 1970-06-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1971-06-18 00:00:00 | Diagnoses | Hyperglycemia (disorder) code=80394007 | **DIABETES** | conditions.csv |
| 1971-06-18 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1971-06-18T21:21:21Z |  | encounters.csv |
| 1971-06-18 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1971-06-18 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1971-06-18 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=48.72 | **DIABETES** | medications.csv |
| 1971-06-18 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1972-06-23 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1972-06-23T21:21:21Z |  | encounters.csv |
| 1972-06-23 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1972-06-23 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1972-06-23 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=313.32 | **DIABETES** | medications.csv |
| 1972-06-23 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1973-06-29 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1973-06-29T21:06:21Z |  | encounters.csv |
| 1973-06-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1973-06-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1973-06-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=2282.88 | **DIABETES** | medications.csv |
| 1973-06-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1974-07-05 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1974-07-05T21:06:21Z |  | encounters.csv |
| 1974-07-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1974-07-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1974-07-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=1054.68 | **DIABETES** | medications.csv |
| 1974-07-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1975-07-11 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1975-07-11T21:06:21Z |  | encounters.csv |
| 1975-07-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1975-07-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1975-07-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=1212.00 | **DIABETES** | medications.csv |
| 1975-07-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1976-07-16 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1976-07-16T21:21:21Z |  | encounters.csv |
| 1976-07-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1976-07-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1976-07-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=771.84 | **DIABETES** | medications.csv |
| 1976-07-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1977-07-22 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1977-07-22T21:06:21Z |  | encounters.csv |
| 1977-07-22 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1977-07-22 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1977-07-22 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=1795.32 | **DIABETES** | medications.csv |
| 1977-07-22 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1978-07-28 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1978-07-28T21:21:21Z |  | encounters.csv |
| 1978-07-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1978-07-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1978-07-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=915.12 | **DIABETES** | medications.csv |
| 1978-07-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1979-08-03 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1979-08-03T21:21:21Z |  | encounters.csv |
| 1979-08-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1979-08-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1979-08-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=2081.64 | **DIABETES** | medications.csv |
| 1979-08-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1980-08-08 00:00:00 | Diagnoses | Neuropathy due to type 2 diabetes mellitus (disorder) code=368581000119106 | **DIABETES** | conditions.csv |
| 1980-08-08 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1980-08-08T21:06:21Z |  | encounters.csv |
| 1980-08-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1980-08-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1980-08-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=12; total cost=489.96 | **DIABETES** | medications.csv |
| 1980-08-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=12; total cost=3161.88 | **HYPERTENSION** | medications.csv |
| 1981-08-14 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1981-08-14T21:06:21Z |  | encounters.csv |
| 1981-08-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1981-08-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1981-08-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=7; total cost=1139.81 | **DIABETES** | medications.csv |
| 1981-08-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=7; total cost=1844.43 | **HYPERTENSION** | medications.csv |
| 1982-03-19 00:00:00 | Diagnoses | Chronic kidney disease stage 1 (disorder) code=431855005 |  | conditions.csv |
| 1982-03-19 00:00:00 | Diagnoses | Diabetic renal disease (disorder) code=127013003 | **DIABETES** | conditions.csv |
| 1982-03-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1982-03-19T21:06:21Z |  | encounters.csv |
| 1982-03-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1982-03-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1982-03-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=5; total cost=2225.60 | **DIABETES** | medications.csv |
| 1982-03-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=5; total cost=1317.45 | **HYPERTENSION** | medications.csv |
| 1982-08-20 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1982-08-20T21:21:21Z |  | encounters.csv |
| 1982-08-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1982-08-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1982-08-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=169.51 | **DIABETES** | medications.csv |
| 1982-08-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1982-10-15 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1982-10-15T21:06:21Z |  | encounters.csv |
| 1982-10-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1982-10-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1982-10-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=10; total cost=3232.70 | **DIABETES** | medications.csv |
| 1982-10-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=10; total cost=2634.90 | **HYPERTENSION** | medications.csv |
| 1982-10-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=10; total cost=4778.30 | **DIABETES** | medications.csv |
| 1983-08-26 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1983-08-26T21:21:21Z |  | encounters.csv |
| 1983-08-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1983-08-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1983-08-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1983-08-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=793.56 | **DIABETES** | medications.csv |
| 1983-08-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 1983-08-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=1842.24 | **DIABETES** | medications.csv |
| 1984-01-13 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1984-01-13T21:06:21Z |  | encounters.csv |
| 1984-01-13 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-01-13 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1984-01-13 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-01-13 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=427.90 | **DIABETES** | medications.csv |
| 1984-01-13 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1984-01-13 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=369.79 | **DIABETES** | medications.csv |
| 1984-03-09 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1984-03-09T21:06:21Z |  | encounters.csv |
| 1984-03-09 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-03-09 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1984-03-09 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-03-09 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1264.32 | **DIABETES** | medications.csv |
| 1984-03-09 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1984-03-09 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=3041.97 | **DIABETES** | medications.csv |
| 1984-07-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1984-07-06T21:06:21Z |  | encounters.csv |
| 1984-07-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-07-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1984-07-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-07-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=103.20 | **DIABETES** | medications.csv |
| 1984-07-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1984-07-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=989.04 | **DIABETES** | medications.csv |
| 1984-08-31 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1984-08-31T21:06:21Z |  | encounters.csv |
| 1984-08-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-08-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1984-08-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-08-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=323.92 | **DIABETES** | medications.csv |
| 1984-08-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1984-08-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=481.25 | **DIABETES** | medications.csv |
| 1984-09-07 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1984-09-07T21:06:21Z |  | encounters.csv |
| 1984-09-07 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-09-07 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1984-09-07 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-09-07 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=28.81 | **DIABETES** | medications.csv |
| 1984-09-07 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1984-09-07 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1233.21 | **DIABETES** | medications.csv |
| 1984-11-02 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1984-11-02T21:06:21Z |  | encounters.csv |
| 1984-11-02 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-11-02 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1984-11-02 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1984-11-02 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=10; total cost=2210.80 | **DIABETES** | medications.csv |
| 1984-11-02 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=10; total cost=2634.90 | **HYPERTENSION** | medications.csv |
| 1984-11-02 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=10; total cost=12852.70 | **DIABETES** | medications.csv |
| 1985-09-06 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1985-09-06T21:21:21Z |  | encounters.csv |
| 1985-09-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1985-09-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1985-09-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1985-09-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=312.01 | **DIABETES** | medications.csv |
| 1985-09-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1985-09-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=912.84 | **DIABETES** | medications.csv |
| 1985-10-04 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1985-10-04T21:06:21Z |  | encounters.csv |
| 1985-10-04 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1985-10-04 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1985-10-04 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1985-10-04 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=182.29 | **DIABETES** | medications.csv |
| 1985-10-04 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1985-10-04 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=625.92 | **DIABETES** | medications.csv |
| 1985-11-01 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1985-11-01T21:06:21Z |  | encounters.csv |
| 1985-11-01 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1985-11-01 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1985-11-01 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1985-11-01 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=99.81 | **DIABETES** | medications.csv |
| 1985-11-01 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1985-11-01 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=2078.28 | **DIABETES** | medications.csv |
| 1986-02-28 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1986-02-28T21:06:21Z |  | encounters.csv |
| 1986-02-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-02-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1986-02-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-02-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=755.72 | **DIABETES** | medications.csv |
| 1986-02-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 1986-02-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=2192.32 | **DIABETES** | medications.csv |
| 1986-07-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1986-07-25T21:06:21Z |  | encounters.csv |
| 1986-07-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-07-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1986-07-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-07-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=187.14 | **DIABETES** | medications.csv |
| 1986-07-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1986-07-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1169.61 | **DIABETES** | medications.csv |
| 1986-08-29 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1986-08-29T21:06:21Z |  | encounters.csv |
| 1986-08-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-08-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1986-08-29 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-08-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=268.54 | **DIABETES** | medications.csv |
| 1986-08-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1986-08-29 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=745.36 | **DIABETES** | medications.csv |
| 1986-09-12 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1986-09-12T21:06:21Z |  | encounters.csv |
| 1986-09-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-09-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1986-09-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1986-09-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=7; total cost=1432.34 | **DIABETES** | medications.csv |
| 1986-09-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=7; total cost=1844.43 | **HYPERTENSION** | medications.csv |
| 1986-09-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=7; total cost=10167.57 | **DIABETES** | medications.csv |
| 1987-04-24 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1987-04-24T21:06:21Z |  | encounters.csv |
| 1987-04-24 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-04-24 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1987-04-24 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-04-24 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=975.06 | **DIABETES** | medications.csv |
| 1987-04-24 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1987-04-24 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=4052.43 | **DIABETES** | medications.csv |
| 1987-07-24 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1987-07-24T21:06:21Z |  | encounters.csv |
| 1987-07-24 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-07-24 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1987-07-24 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-07-24 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=89.43 | **DIABETES** | medications.csv |
| 1987-07-24 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1987-07-24 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=398.18 | **DIABETES** | medications.csv |
| 1987-09-18 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1987-09-18T21:06:21Z |  | encounters.csv |
| 1987-09-18 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-09-18 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1987-09-18 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-09-18 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=419.83 | **DIABETES** | medications.csv |
| 1987-09-18 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1987-09-18 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1219.35 | **DIABETES** | medications.csv |
| 1987-10-23 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1987-10-23T21:06:21Z |  | encounters.csv |
| 1987-10-23 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-10-23 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1987-10-23 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1987-10-23 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=61.98 | **DIABETES** | medications.csv |
| 1987-10-23 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1987-10-23 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=2862.75 | **DIABETES** | medications.csv |
| 1988-01-22 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1988-01-22T21:06:21Z |  | encounters.csv |
| 1988-01-22 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-01-22 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1988-01-22 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-01-22 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=352.35 | **DIABETES** | medications.csv |
| 1988-01-22 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1988-01-22 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=484.58 | **DIABETES** | medications.csv |
| 1988-02-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1988-02-19T21:06:21Z |  | encounters.csv |
| 1988-02-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-02-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1988-02-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-02-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=104.70 | **DIABETES** | medications.csv |
| 1988-02-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1988-02-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=3324.57 | **DIABETES** | medications.csv |
| 1988-05-20 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1988-05-20T21:06:21Z |  | encounters.csv |
| 1988-05-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-05-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1988-05-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-05-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=150.40 | **DIABETES** | medications.csv |
| 1988-05-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1988-05-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1602.52 | **DIABETES** | medications.csv |
| 1988-07-15 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1988-07-15T21:06:21Z |  | encounters.csv |
| 1988-07-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-07-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1988-07-15 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-07-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=289.85 | **DIABETES** | medications.csv |
| 1988-07-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1988-07-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=768.79 | **DIABETES** | medications.csv |
| 1988-08-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1988-08-26T21:06:21Z |  | encounters.csv |
| 1988-08-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-08-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1988-08-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-08-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=212.81 | **DIABETES** | medications.csv |
| 1988-08-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1988-08-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=463.47 | **DIABETES** | medications.csv |
| 1988-09-23 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1988-09-23T21:06:21Z |  | encounters.csv |
| 1988-09-23 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-09-23 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1988-09-23 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-09-23 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=563.86 | **DIABETES** | medications.csv |
| 1988-09-23 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 1988-09-23 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=2140.06 | **DIABETES** | medications.csv |
| 1988-12-16 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1988-12-16T21:06:21Z |  | encounters.csv |
| 1988-12-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-12-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1988-12-16 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1988-12-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=224.97 | **DIABETES** | medications.csv |
| 1988-12-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1988-12-16 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=3364.35 | **DIABETES** | medications.csv |
| 1989-03-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1989-03-17T21:06:21Z |  | encounters.csv |
| 1989-03-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-03-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1989-03-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-03-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=353.26 | **DIABETES** | medications.csv |
| 1989-03-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 1989-03-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=786.64 | **DIABETES** | medications.csv |
| 1989-06-09 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1989-06-09T21:06:21Z |  | encounters.csv |
| 1989-06-09 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-06-09 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1989-06-09 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-06-09 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=353.67 | **DIABETES** | medications.csv |
| 1989-06-09 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1989-06-09 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1425.96 | **DIABETES** | medications.csv |
| 1989-09-29 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1989-09-29T21:21:21Z |  | encounters.csv |
| 1989-09-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-09-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1989-09-29 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-09-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=30.16 | **DIABETES** | medications.csv |
| 1989-09-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1989-09-29 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=628.35 | **DIABETES** | medications.csv |
| 1989-10-13 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1989-10-13T21:06:21Z |  | encounters.csv |
| 1989-10-13 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-10-13 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1989-10-13 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-10-13 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=312.41 | **DIABETES** | medications.csv |
| 1989-10-13 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1989-10-13 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1360.70 | **DIABETES** | medications.csv |
| 1989-12-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1989-12-08T21:06:21Z |  | encounters.csv |
| 1989-12-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-12-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1989-12-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1989-12-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=7; total cost=796.74 | **DIABETES** | medications.csv |
| 1989-12-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=7; total cost=1844.43 | **HYPERTENSION** | medications.csv |
| 1989-12-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=7; total cost=3014.90 | **DIABETES** | medications.csv |
| 1990-07-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1990-07-06T21:06:21Z |  | encounters.csv |
| 1990-07-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1990-07-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1990-07-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1990-07-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=985.71 | **DIABETES** | medications.csv |
| 1990-07-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1990-07-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1914.60 | **DIABETES** | medications.csv |
| 1990-10-05 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1990-10-05T21:21:21Z |  | encounters.csv |
| 1990-10-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1990-10-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1990-10-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1990-10-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=53.20 | **DIABETES** | medications.csv |
| 1990-10-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1990-10-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=327.22 | **DIABETES** | medications.csv |
| 1990-10-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1990-10-12T21:06:21Z |  | encounters.csv |
| 1990-10-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1990-10-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1990-10-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1990-10-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=7; total cost=2487.17 | **DIABETES** | medications.csv |
| 1990-10-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=7; total cost=1844.43 | **HYPERTENSION** | medications.csv |
| 1990-10-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=7; total cost=10161.48 | **DIABETES** | medications.csv |
| 1991-05-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1991-05-31T21:06:21Z |  | encounters.csv |
| 1991-05-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-05-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1991-05-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-05-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=773.67 | **DIABETES** | medications.csv |
| 1991-05-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1991-05-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=726.15 | **DIABETES** | medications.csv |
| 1991-09-27 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1991-09-27T21:06:21Z |  | encounters.csv |
| 1991-09-27 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-09-27 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1991-09-27 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-09-27 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=127.19 | **DIABETES** | medications.csv |
| 1991-09-27 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1991-09-27 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=333.28 | **DIABETES** | medications.csv |
| 1991-10-11 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1991-10-11T21:06:21Z |  | encounters.csv |
| 1991-10-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-10-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1991-10-11 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-10-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=380.48 | **DIABETES** | medications.csv |
| 1991-10-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1991-10-11 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1252.89 | **DIABETES** | medications.csv |
| 1991-11-01 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1991-11-01T21:06:21Z |  | encounters.csv |
| 1991-11-01 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-11-01 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1991-11-01 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1991-11-01 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1563.42 | **DIABETES** | medications.csv |
| 1991-11-01 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1991-11-01 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=2389.95 | **DIABETES** | medications.csv |
| 1992-01-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1992-01-31T21:06:21Z |  | encounters.csv |
| 1992-01-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-01-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1992-01-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-01-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=149.15 | **DIABETES** | medications.csv |
| 1992-01-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1992-01-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1003.69 | **DIABETES** | medications.csv |
| 1992-02-28 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1992-02-28T21:06:21Z |  | encounters.csv |
| 1992-02-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-02-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1992-02-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-02-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=6; total cost=1458.36 | **DIABETES** | medications.csv |
| 1992-02-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=6; total cost=1580.94 | **HYPERTENSION** | medications.csv |
| 1992-02-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=6; total cost=8150.70 | **DIABETES** | medications.csv |
| 1992-08-28 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1992-08-28T21:06:21Z |  | encounters.csv |
| 1992-08-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-08-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1992-08-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-08-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=217.55 | **DIABETES** | medications.csv |
| 1992-08-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1992-08-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1039.27 | **DIABETES** | medications.csv |
| 1992-09-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1992-09-25T21:06:21Z |  | encounters.csv |
| 1992-09-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-09-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1992-09-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-09-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=476.40 | **DIABETES** | medications.csv |
| 1992-09-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1992-09-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1234.57 | **DIABETES** | medications.csv |
| 1992-10-16 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1992-10-16T21:06:21Z |  | encounters.csv |
| 1992-10-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-10-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1992-10-16 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-10-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=308.72 | **DIABETES** | medications.csv |
| 1992-10-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1992-10-16 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=265.25 | **DIABETES** | medications.csv |
| 1992-10-23 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1992-10-23T21:06:21Z |  | encounters.csv |
| 1992-10-23 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-10-23 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1992-10-23 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1992-10-23 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=267.69 | **DIABETES** | medications.csv |
| 1992-10-23 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1992-10-23 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=4860.99 | **DIABETES** | medications.csv |
| 1993-02-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1993-02-19T21:06:21Z |  | encounters.csv |
| 1993-02-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-02-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1993-02-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-02-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=917.96 | **DIABETES** | medications.csv |
| 1993-02-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 1993-02-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=2474.96 | **DIABETES** | medications.csv |
| 1993-06-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1993-06-25T21:06:21Z |  | encounters.csv |
| 1993-06-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-06-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1993-06-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-06-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=54.09 | **DIABETES** | medications.csv |
| 1993-06-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1993-06-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=774.06 | **DIABETES** | medications.csv |
| 1993-08-20 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1993-08-20T21:06:21Z |  | encounters.csv |
| 1993-08-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-08-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1993-08-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-08-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=152.73 | **DIABETES** | medications.csv |
| 1993-08-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1993-08-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1436.33 | **DIABETES** | medications.csv |
| 1993-09-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1993-09-17T21:06:21Z |  | encounters.csv |
| 1993-09-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-09-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1993-09-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-09-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=353.11 | **DIABETES** | medications.csv |
| 1993-09-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1993-09-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1372.00 | **DIABETES** | medications.csv |
| 1993-10-22 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1993-10-22T21:21:21Z |  | encounters.csv |
| 1993-10-22 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-10-22 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1993-10-22 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-10-22 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=96.91 | **DIABETES** | medications.csv |
| 1993-10-22 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1993-10-22 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1098.83 | **DIABETES** | medications.csv |
| 1993-11-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1993-11-19T21:06:21Z |  | encounters.csv |
| 1993-11-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-11-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1993-11-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1993-11-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=399.85 | **DIABETES** | medications.csv |
| 1993-11-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1993-11-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=927.16 | **DIABETES** | medications.csv |
| 1994-01-14 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1994-01-14T21:06:21Z |  | encounters.csv |
| 1994-01-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-01-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1994-01-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-01-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=772.46 | **DIABETES** | medications.csv |
| 1994-01-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 1994-01-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=631.84 | **DIABETES** | medications.csv |
| 1994-03-18 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1994-03-18T21:06:21Z |  | encounters.csv |
| 1994-03-18 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-03-18 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1994-03-18 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-03-18 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1145.16 | **DIABETES** | medications.csv |
| 1994-03-18 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1994-03-18 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1273.83 | **DIABETES** | medications.csv |
| 1994-06-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1994-06-17T21:06:21Z |  | encounters.csv |
| 1994-06-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-06-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1994-06-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-06-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=147.80 | **DIABETES** | medications.csv |
| 1994-06-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 1994-06-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=1798.44 | **DIABETES** | medications.csv |
| 1994-10-28 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1994-10-28T21:06:21Z |  | encounters.csv |
| 1994-10-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-10-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1994-10-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1994-10-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=670.52 | **DIABETES** | medications.csv |
| 1994-10-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 1994-10-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=2275.68 | **DIABETES** | medications.csv |
| 1995-03-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1995-03-17T21:06:21Z |  | encounters.csv |
| 1995-03-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-03-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1995-03-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-03-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1268.13 | **DIABETES** | medications.csv |
| 1995-03-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1995-03-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1519.53 | **DIABETES** | medications.csv |
| 1995-07-14 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1995-07-14T21:06:21Z |  | encounters.csv |
| 1995-07-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-07-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1995-07-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-07-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=270.66 | **DIABETES** | medications.csv |
| 1995-07-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1995-07-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=611.04 | **DIABETES** | medications.csv |
| 1995-08-11 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1995-08-11T21:06:21Z |  | encounters.csv |
| 1995-08-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-08-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1995-08-11 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-08-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=19.28 | **DIABETES** | medications.csv |
| 1995-08-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1995-08-11 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1672.80 | **DIABETES** | medications.csv |
| 1995-09-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1995-09-08T21:06:21Z |  | encounters.csv |
| 1995-09-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-09-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1995-09-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-09-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=233.75 | **DIABETES** | medications.csv |
| 1995-09-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1995-09-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1293.47 | **DIABETES** | medications.csv |
| 1995-11-03 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1995-11-03T21:06:21Z |  | encounters.csv |
| 1995-11-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-11-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1995-11-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1995-11-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=359.50 | **DIABETES** | medications.csv |
| 1995-11-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 1995-11-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=3297.02 | **DIABETES** | medications.csv |
| 1996-01-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1996-01-19T21:06:21Z |  | encounters.csv |
| 1996-01-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-01-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1996-01-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-01-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=545.61 | **DIABETES** | medications.csv |
| 1996-01-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1996-01-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=612.00 | **DIABETES** | medications.csv |
| 1996-03-15 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1996-03-15T21:06:21Z |  | encounters.csv |
| 1996-03-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-03-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1996-03-15 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-03-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=130.96 | **DIABETES** | medications.csv |
| 1996-03-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1996-03-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1003.88 | **DIABETES** | medications.csv |
| 1996-05-03 00:00:00 | Diagnoses | Atrial Fibrillation code=49436004 |  | conditions.csv |
| 1996-05-03 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=1996-05-03T21:06:21Z |  | encounters.csv |
| 1996-05-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=50.13 |  | medications.csv |
| 1996-05-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=251.80 |  | medications.csv |
| 1996-05-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=165.51 |  | medications.csv |
| 1996-05-10 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1996-05-10T21:21:21Z |  | encounters.csv |
| 1996-05-10 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-05-10 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1996-05-10 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1996-05-10 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-05-10 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1996-05-10 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1996-05-10 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=6; total cost=1612.92 | **DIABETES** | medications.csv |
| 1996-05-10 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=6; total cost=1580.94 | **HYPERTENSION** | medications.csv |
| 1996-05-10 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=6; total cost=360.60 |  | medications.csv |
| 1996-05-10 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=6; total cost=1407.96 | **DIABETES** | medications.csv |
| 1996-05-10 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=6; total cost=457.26 |  | medications.csv |
| 1996-05-10 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=6; total cost=297.72 |  | medications.csv |
| 1996-11-08 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1996-11-08T21:36:21Z |  | encounters.csv |
| 1996-11-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-11-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1996-11-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1996-11-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-11-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1996-11-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1996-11-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=209.03 | **DIABETES** | medications.csv |
| 1996-11-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1996-11-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=66.75 |  | medications.csv |
| 1996-11-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1100.53 | **DIABETES** | medications.csv |
| 1996-11-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=181.02 |  | medications.csv |
| 1996-11-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=14.31 |  | medications.csv |
| 1996-11-29 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1996-11-29T21:21:21Z |  | encounters.csv |
| 1996-11-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-11-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1996-11-29 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1996-11-29 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1996-11-29 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1996-11-29 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1996-11-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=431.11 | **DIABETES** | medications.csv |
| 1996-11-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1996-11-29 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=146.97 |  | medications.csv |
| 1996-11-29 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=895.31 | **DIABETES** | medications.csv |
| 1996-11-29 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=194.90 |  | medications.csv |
| 1996-11-29 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=108.39 |  | medications.csv |
| 1997-01-03 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-01-03T21:21:21Z |  | encounters.csv |
| 1997-01-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-01-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-01-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-01-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-01-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-01-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-01-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1319.49 | **DIABETES** | medications.csv |
| 1997-01-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1997-01-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=129.51 |  | medications.csv |
| 1997-01-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=5403.69 | **DIABETES** | medications.csv |
| 1997-01-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=255.54 |  | medications.csv |
| 1997-01-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=426.99 |  | medications.csv |
| 1997-05-02 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-05-02T21:21:21Z |  | encounters.csv |
| 1997-05-02 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-05-02 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-05-02 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-05-02 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-05-02 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-05-02 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-05-02 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=174.69 | **DIABETES** | medications.csv |
| 1997-05-02 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-05-02 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=124.03 |  | medications.csv |
| 1997-05-02 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1282.85 | **DIABETES** | medications.csv |
| 1997-05-02 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=107.57 |  | medications.csv |
| 1997-05-02 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=190.50 |  | medications.csv |
| 1997-06-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-06-06T21:21:21Z |  | encounters.csv |
| 1997-06-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-06-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-06-06 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-06-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-06-06 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-06-06 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-06-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=329.77 | **DIABETES** | medications.csv |
| 1997-06-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-06-06 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=125.28 |  | medications.csv |
| 1997-06-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=879.73 | **DIABETES** | medications.csv |
| 1997-06-06 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=175.49 |  | medications.csv |
| 1997-06-06 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=86.94 |  | medications.csv |
| 1997-06-27 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-06-27T21:21:21Z |  | encounters.csv |
| 1997-06-27 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-06-27 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-06-27 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-06-27 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-06-27 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-06-27 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-06-27 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=316.68 | **DIABETES** | medications.csv |
| 1997-06-27 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 1997-06-27 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=95.20 |  | medications.csv |
| 1997-06-27 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=904.80 | **DIABETES** | medications.csv |
| 1997-06-27 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=218.52 |  | medications.csv |
| 1997-06-27 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=320.04 |  | medications.csv |
| 1997-09-05 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-09-05T21:21:21Z |  | encounters.csv |
| 1997-09-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-09-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-09-05 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-09-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-09-05 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-09-05 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-09-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=142.83 | **DIABETES** | medications.csv |
| 1997-09-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-09-05 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=97.11 |  | medications.csv |
| 1997-09-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=809.49 | **DIABETES** | medications.csv |
| 1997-09-05 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=128.59 |  | medications.csv |
| 1997-09-05 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=184.38 |  | medications.csv |
| 1997-10-03 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-10-03T21:21:21Z |  | encounters.csv |
| 1997-10-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-10-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-10-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-10-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-10-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-10-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-10-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=6.67 | **DIABETES** | medications.csv |
| 1997-10-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-10-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=93.57 |  | medications.csv |
| 1997-10-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1078.93 | **DIABETES** | medications.csv |
| 1997-10-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=64.84 |  | medications.csv |
| 1997-10-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=27.70 |  | medications.csv |
| 1997-10-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-10-31T21:21:21Z |  | encounters.csv |
| 1997-10-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-10-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-10-31 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-10-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-10-31 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-10-31 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-10-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=299.70 | **DIABETES** | medications.csv |
| 1997-10-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-10-31 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=96.34 |  | medications.csv |
| 1997-10-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=811.45 | **DIABETES** | medications.csv |
| 1997-10-31 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=50.73 |  | medications.csv |
| 1997-10-31 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=178.52 |  | medications.csv |
| 1997-11-14 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1997-11-14T21:21:21Z |  | encounters.csv |
| 1997-11-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-11-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-11-14 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-11-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-11-14 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-11-14 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-11-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=78.06 | **DIABETES** | medications.csv |
| 1997-11-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-11-14 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=128.34 |  | medications.csv |
| 1997-11-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=669.40 | **DIABETES** | medications.csv |
| 1997-11-14 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=57.10 |  | medications.csv |
| 1997-11-14 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=124.18 |  | medications.csv |
| 1997-12-05 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-12-05T21:21:21Z |  | encounters.csv |
| 1997-12-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-12-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-12-05 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-12-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-12-05 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-12-05 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-12-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=565.39 | **DIABETES** | medications.csv |
| 1997-12-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-12-05 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=43.37 |  | medications.csv |
| 1997-12-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=589.81 | **DIABETES** | medications.csv |
| 1997-12-05 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=96.60 |  | medications.csv |
| 1997-12-05 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=154.41 |  | medications.csv |
| 1997-12-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1997-12-26T21:21:21Z |  | encounters.csv |
| 1997-12-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-12-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1997-12-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1997-12-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1997-12-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1997-12-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1997-12-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=226.05 | **DIABETES** | medications.csv |
| 1997-12-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1997-12-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=62.51 |  | medications.csv |
| 1997-12-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1162.86 | **DIABETES** | medications.csv |
| 1997-12-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=56.14 |  | medications.csv |
| 1997-12-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=121.72 |  | medications.csv |
| 1998-01-23 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1998-01-23T21:21:21Z |  | encounters.csv |
| 1998-01-23 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-01-23 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-01-23 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-01-23 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-01-23 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-01-23 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-01-23 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=412.96 | **DIABETES** | medications.csv |
| 1998-01-23 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1998-01-23 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=60.63 |  | medications.csv |
| 1998-01-23 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=245.94 | **DIABETES** | medications.csv |
| 1998-01-23 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=37.16 |  | medications.csv |
| 1998-01-23 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=26.63 |  | medications.csv |
| 1998-03-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1998-03-06T21:21:21Z |  | encounters.csv |
| 1998-03-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-03-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-03-06 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-03-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-03-06 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-03-06 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-03-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=107.90 | **DIABETES** | medications.csv |
| 1998-03-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1998-03-06 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=85.75 |  | medications.csv |
| 1998-03-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=298.20 | **DIABETES** | medications.csv |
| 1998-03-06 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=99.23 |  | medications.csv |
| 1998-03-06 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=95.64 |  | medications.csv |
| 1998-04-03 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1998-04-03T21:21:21Z |  | encounters.csv |
| 1998-04-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-04-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-04-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-04-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-04-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-04-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-04-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=352.08 | **DIABETES** | medications.csv |
| 1998-04-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1998-04-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=21.89 |  | medications.csv |
| 1998-04-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1131.35 | **DIABETES** | medications.csv |
| 1998-04-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=73.77 |  | medications.csv |
| 1998-04-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=136.32 |  | medications.csv |
| 1998-05-29 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1998-05-29T21:21:21Z |  | encounters.csv |
| 1998-05-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-05-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-05-29 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-05-29 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-05-29 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-05-29 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-05-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=205.74 | **DIABETES** | medications.csv |
| 1998-05-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1998-05-29 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=33.63 |  | medications.csv |
| 1998-05-29 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=477.03 | **DIABETES** | medications.csv |
| 1998-05-29 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=172.13 |  | medications.csv |
| 1998-05-29 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=199.08 |  | medications.csv |
| 1998-07-03 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1998-07-03T21:21:21Z |  | encounters.csv |
| 1998-07-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-07-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-07-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-07-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-07-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-07-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-07-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=159.61 | **DIABETES** | medications.csv |
| 1998-07-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1998-07-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=121.34 |  | medications.csv |
| 1998-07-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1275.96 | **DIABETES** | medications.csv |
| 1998-07-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=34.39 |  | medications.csv |
| 1998-07-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=43.31 |  | medications.csv |
| 1998-07-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1998-07-31T21:21:21Z |  | encounters.csv |
| 1998-07-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-07-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-07-31 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-07-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-07-31 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-07-31 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-07-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=177.57 | **DIABETES** | medications.csv |
| 1998-07-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1998-07-31 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=231.39 |  | medications.csv |
| 1998-07-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=731.28 | **DIABETES** | medications.csv |
| 1998-07-31 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=127.80 |  | medications.csv |
| 1998-07-31 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=576.93 |  | medications.csv |
| 1998-11-20 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1998-11-20T21:36:21Z |  | encounters.csv |
| 1998-11-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-11-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-11-20 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-11-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-11-20 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-11-20 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-11-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=328.60 | **DIABETES** | medications.csv |
| 1998-11-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1998-11-20 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=109.77 |  | medications.csv |
| 1998-11-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1203.73 | **DIABETES** | medications.csv |
| 1998-11-20 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=119.86 |  | medications.csv |
| 1998-11-20 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=44.71 |  | medications.csv |
| 1998-12-04 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1998-12-04T21:21:21Z |  | encounters.csv |
| 1998-12-04 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-12-04 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1998-12-04 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1998-12-04 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1998-12-04 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1998-12-04 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1998-12-04 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=27.75 | **DIABETES** | medications.csv |
| 1998-12-04 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1998-12-04 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=102.19 |  | medications.csv |
| 1998-12-04 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=706.15 | **DIABETES** | medications.csv |
| 1998-12-04 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=48.20 |  | medications.csv |
| 1998-12-04 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=67.81 |  | medications.csv |
| 1999-01-01 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1999-01-01T21:21:21Z |  | encounters.csv |
| 1999-01-01 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-01-01 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1999-01-01 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1999-01-01 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-01-01 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1999-01-01 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1999-01-01 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=44.70 | **DIABETES** | medications.csv |
| 1999-01-01 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1999-01-01 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=82.01 |  | medications.csv |
| 1999-01-01 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=372.43 | **DIABETES** | medications.csv |
| 1999-01-01 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=39.16 |  | medications.csv |
| 1999-01-01 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=18.54 |  | medications.csv |
| 1999-02-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1999-02-19T21:21:21Z |  | encounters.csv |
| 1999-02-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-02-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1999-02-19 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1999-02-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-02-19 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1999-02-19 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1999-02-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=350.02 | **DIABETES** | medications.csv |
| 1999-02-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1999-02-19 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=50.78 |  | medications.csv |
| 1999-02-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1042.07 | **DIABETES** | medications.csv |
| 1999-02-19 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=39.89 |  | medications.csv |
| 1999-02-19 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=169.57 |  | medications.csv |
| 1999-03-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1999-03-26T21:21:21Z |  | encounters.csv |
| 1999-03-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-03-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1999-03-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1999-03-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-03-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1999-03-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1999-03-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=397.35 | **DIABETES** | medications.csv |
| 1999-03-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 1999-03-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=153.09 |  | medications.csv |
| 1999-03-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=823.41 | **DIABETES** | medications.csv |
| 1999-03-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=477.78 |  | medications.csv |
| 1999-03-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=319.20 |  | medications.csv |
| 1999-06-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1999-06-25T21:21:21Z |  | encounters.csv |
| 1999-06-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-06-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1999-06-25 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1999-06-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-06-25 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1999-06-25 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1999-06-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=39.84 | **DIABETES** | medications.csv |
| 1999-06-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1999-06-25 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=83.33 |  | medications.csv |
| 1999-06-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=757.05 | **DIABETES** | medications.csv |
| 1999-06-25 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=237.74 |  | medications.csv |
| 1999-06-25 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=118.72 |  | medications.csv |
| 1999-08-20 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1999-08-20T21:21:21Z |  | encounters.csv |
| 1999-08-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-08-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1999-08-20 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1999-08-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-08-20 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1999-08-20 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1999-08-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=104.24 | **DIABETES** | medications.csv |
| 1999-08-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1999-08-20 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=13.43 |  | medications.csv |
| 1999-08-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=161.88 | **DIABETES** | medications.csv |
| 1999-08-20 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=81.77 |  | medications.csv |
| 1999-08-20 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=74.99 |  | medications.csv |
| 1999-09-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=1999-09-17T21:21:21Z |  | encounters.csv |
| 1999-09-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-09-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1999-09-17 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1999-09-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-09-17 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1999-09-17 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1999-09-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=376.44 | **DIABETES** | medications.csv |
| 1999-09-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 1999-09-17 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=296.60 |  | medications.csv |
| 1999-09-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=1141.92 | **DIABETES** | medications.csv |
| 1999-09-17 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=537.28 |  | medications.csv |
| 1999-09-17 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=181.68 |  | medications.csv |
| 1999-11-26 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=1999-11-26T21:21:21Z |  | encounters.csv |
| 1999-11-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-11-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 1999-11-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 1999-11-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 1999-11-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 1999-11-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 1999-11-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=164.25 | **DIABETES** | medications.csv |
| 1999-11-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 1999-11-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=59.26 |  | medications.csv |
| 1999-11-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=392.69 | **DIABETES** | medications.csv |
| 1999-11-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=77.54 |  | medications.csv |
| 1999-11-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=132.27 |  | medications.csv |
| 2000-01-14 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2000-01-14T21:21:21Z |  | encounters.csv |
| 2000-01-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-01-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2000-01-14 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2000-01-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-01-14 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2000-01-14 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2000-01-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=281.00 | **DIABETES** | medications.csv |
| 2000-01-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2000-01-14 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=131.48 |  | medications.csv |
| 2000-01-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=2998.98 | **DIABETES** | medications.csv |
| 2000-01-14 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=29.68 |  | medications.csv |
| 2000-01-14 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=107.30 |  | medications.csv |
| 2000-03-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2000-03-17T21:21:21Z |  | encounters.csv |
| 2000-03-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-03-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2000-03-17 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2000-03-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-03-17 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2000-03-17 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2000-03-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=374.05 | **DIABETES** | medications.csv |
| 2000-03-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2000-03-17 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=51.45 |  | medications.csv |
| 2000-03-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=908.96 | **DIABETES** | medications.csv |
| 2000-03-17 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=135.20 |  | medications.csv |
| 2000-03-17 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=138.84 |  | medications.csv |
| 2000-04-21 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2000-04-21T21:21:21Z |  | encounters.csv |
| 2000-04-21 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-04-21 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2000-04-21 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2000-04-21 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-04-21 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2000-04-21 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2000-04-21 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=311.52 | **DIABETES** | medications.csv |
| 2000-04-21 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2000-04-21 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=27.75 |  | medications.csv |
| 2000-04-21 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=322.25 | **DIABETES** | medications.csv |
| 2000-04-21 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=21.56 |  | medications.csv |
| 2000-04-21 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=83.02 |  | medications.csv |
| 2000-05-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2000-05-12T21:21:21Z |  | encounters.csv |
| 2000-05-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-05-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2000-05-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2000-05-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-05-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2000-05-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2000-05-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=343.24 | **DIABETES** | medications.csv |
| 2000-05-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2000-05-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=177.60 |  | medications.csv |
| 2000-05-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=6346.32 | **DIABETES** | medications.csv |
| 2000-05-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=608.36 |  | medications.csv |
| 2000-05-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=718.48 |  | medications.csv |
| 2000-09-15 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2000-09-15T21:21:21Z |  | encounters.csv |
| 2000-09-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-09-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2000-09-15 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2000-09-15 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-09-15 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2000-09-15 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2000-09-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=34.34 | **DIABETES** | medications.csv |
| 2000-09-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2000-09-15 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=281.02 |  | medications.csv |
| 2000-09-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=1364.74 | **DIABETES** | medications.csv |
| 2000-09-15 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=197.58 |  | medications.csv |
| 2000-09-15 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=16.16 |  | medications.csv |
| 2000-12-01 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2000-12-01T21:36:21Z |  | encounters.csv |
| 2000-12-01 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-12-01 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2000-12-01 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2000-12-01 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2000-12-01 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2000-12-01 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2000-12-01 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=117.98 | **DIABETES** | medications.csv |
| 2000-12-01 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2000-12-01 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=33.22 |  | medications.csv |
| 2000-12-01 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=284.70 | **DIABETES** | medications.csv |
| 2000-12-01 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=94.14 |  | medications.csv |
| 2000-12-01 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=16.67 |  | medications.csv |
| 2001-01-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2001-01-12T21:21:21Z |  | encounters.csv |
| 2001-01-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-01-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2001-01-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2001-01-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-01-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2001-01-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2001-01-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=68.95 | **DIABETES** | medications.csv |
| 2001-01-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2001-01-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=44.01 |  | medications.csv |
| 2001-01-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=544.52 | **DIABETES** | medications.csv |
| 2001-01-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=71.57 |  | medications.csv |
| 2001-01-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=47.78 |  | medications.csv |
| 2001-02-16 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2001-02-16T21:21:21Z |  | encounters.csv |
| 2001-02-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-02-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2001-02-16 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2001-02-16 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-02-16 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2001-02-16 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2001-02-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1116.12 | **DIABETES** | medications.csv |
| 2001-02-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2001-02-16 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=193.47 |  | medications.csv |
| 2001-02-16 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1408.41 | **DIABETES** | medications.csv |
| 2001-02-16 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=219.12 |  | medications.csv |
| 2001-02-16 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=114.30 |  | medications.csv |
| 2001-06-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2001-06-08T21:21:21Z |  | encounters.csv |
| 2001-06-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-06-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2001-06-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2001-06-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-06-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2001-06-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2001-06-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=435.63 | **DIABETES** | medications.csv |
| 2001-06-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2001-06-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=116.67 |  | medications.csv |
| 2001-06-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=2084.73 | **DIABETES** | medications.csv |
| 2001-06-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=96.81 |  | medications.csv |
| 2001-06-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=529.71 |  | medications.csv |
| 2001-09-14 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2001-09-14T21:21:21Z |  | encounters.csv |
| 2001-09-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-09-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2001-09-14 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2001-09-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-09-14 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2001-09-14 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2001-09-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=235.08 | **DIABETES** | medications.csv |
| 2001-09-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2001-09-14 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=82.71 |  | medications.csv |
| 2001-09-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1439.32 | **DIABETES** | medications.csv |
| 2001-09-14 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=21.17 |  | medications.csv |
| 2001-09-14 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=36.35 |  | medications.csv |
| 2001-11-09 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2001-11-09T21:21:21Z |  | encounters.csv |
| 2001-11-09 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-11-09 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2001-11-09 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2001-11-09 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-11-09 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2001-11-09 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2001-11-09 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=81.24 | **DIABETES** | medications.csv |
| 2001-11-09 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2001-11-09 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=99.86 |  | medications.csv |
| 2001-11-09 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=314.52 | **DIABETES** | medications.csv |
| 2001-11-09 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=141.41 |  | medications.csv |
| 2001-11-09 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=127.34 |  | medications.csv |
| 2001-12-07 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2001-12-07T21:36:21Z |  | encounters.csv |
| 2001-12-07 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-12-07 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2001-12-07 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2001-12-07 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-12-07 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2001-12-07 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2001-12-07 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=129.62 | **DIABETES** | medications.csv |
| 2001-12-07 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2001-12-07 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=70.31 |  | medications.csv |
| 2001-12-07 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=567.70 | **DIABETES** | medications.csv |
| 2001-12-07 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=115.07 |  | medications.csv |
| 2001-12-07 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=170.72 |  | medications.csv |
| 2001-12-21 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2001-12-21T21:21:21Z |  | encounters.csv |
| 2001-12-21 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-12-21 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2001-12-21 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2001-12-21 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2001-12-21 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2001-12-21 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2001-12-21 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=93.29 | **DIABETES** | medications.csv |
| 2001-12-21 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2001-12-21 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=66.90 |  | medications.csv |
| 2001-12-21 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=458.60 | **DIABETES** | medications.csv |
| 2001-12-21 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=203.67 |  | medications.csv |
| 2001-12-21 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=52.47 |  | medications.csv |
| 2002-01-11 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2002-01-11T21:21:21Z |  | encounters.csv |
| 2002-01-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-01-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-01-11 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-01-11 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-01-11 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-01-11 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-01-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=373.24 | **DIABETES** | medications.csv |
| 2002-01-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2002-01-11 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=36.75 |  | medications.csv |
| 2002-01-11 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1189.29 | **DIABETES** | medications.csv |
| 2002-01-11 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=150.34 |  | medications.csv |
| 2002-01-11 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=129.25 |  | medications.csv |
| 2002-02-01 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2002-02-01T21:21:21Z |  | encounters.csv |
| 2002-02-01 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-02-01 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-02-01 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-02-01 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-02-01 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-02-01 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-02-01 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=201.64 | **DIABETES** | medications.csv |
| 2002-02-01 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2002-02-01 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=41.06 |  | medications.csv |
| 2002-02-01 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=569.43 | **DIABETES** | medications.csv |
| 2002-02-01 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=178.97 |  | medications.csv |
| 2002-02-01 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=66.95 |  | medications.csv |
| 2002-03-15 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2002-03-15T21:21:21Z |  | encounters.csv |
| 2002-03-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-03-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-03-15 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-03-15 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-03-15 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-03-15 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-03-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=750.96 | **DIABETES** | medications.csv |
| 2002-03-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2002-03-15 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=81.42 |  | medications.csv |
| 2002-03-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=4343.04 | **DIABETES** | medications.csv |
| 2002-03-15 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=372.78 |  | medications.csv |
| 2002-03-15 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=376.86 |  | medications.csv |
| 2002-07-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2002-07-12T21:21:21Z |  | encounters.csv |
| 2002-07-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-07-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-07-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-07-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-07-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-07-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-07-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=116.50 | **DIABETES** | medications.csv |
| 2002-07-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2002-07-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=64.18 |  | medications.csv |
| 2002-07-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=476.20 | **DIABETES** | medications.csv |
| 2002-07-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=148.24 |  | medications.csv |
| 2002-07-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=219.82 |  | medications.csv |
| 2002-10-04 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2002-10-04T21:21:21Z |  | encounters.csv |
| 2002-10-04 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-10-04 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-10-04 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-10-04 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-10-04 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-10-04 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-10-04 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=291.96 | **DIABETES** | medications.csv |
| 2002-10-04 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2002-10-04 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=57.96 |  | medications.csv |
| 2002-10-04 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=764.67 | **DIABETES** | medications.csv |
| 2002-10-04 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=24.93 |  | medications.csv |
| 2002-10-04 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=225.45 |  | medications.csv |
| 2002-11-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2002-11-08T21:21:21Z |  | encounters.csv |
| 2002-11-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-11-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-11-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-11-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-11-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-11-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-11-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=107.17 | **DIABETES** | medications.csv |
| 2002-11-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2002-11-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=31.51 |  | medications.csv |
| 2002-11-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1310.43 | **DIABETES** | medications.csv |
| 2002-11-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=85.04 |  | medications.csv |
| 2002-11-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=183.99 |  | medications.csv |
| 2002-11-29 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2002-11-29T21:21:21Z |  | encounters.csv |
| 2002-11-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-11-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-11-29 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-11-29 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-11-29 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-11-29 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-11-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=201.71 | **DIABETES** | medications.csv |
| 2002-11-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2002-11-29 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=115.70 |  | medications.csv |
| 2002-11-29 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=777.44 | **DIABETES** | medications.csv |
| 2002-11-29 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=27.97 |  | medications.csv |
| 2002-11-29 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=189.04 |  | medications.csv |
| 2002-12-13 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2002-12-13T21:21:21Z |  | encounters.csv |
| 2002-12-13 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-12-13 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2002-12-13 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2002-12-13 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2002-12-13 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2002-12-13 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2002-12-13 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=585.87 | **DIABETES** | medications.csv |
| 2002-12-13 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2002-12-13 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=82.21 |  | medications.csv |
| 2002-12-13 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=899.76 | **DIABETES** | medications.csv |
| 2002-12-13 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=214.18 |  | medications.csv |
| 2002-12-13 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=41.15 |  | medications.csv |
| 2003-01-10 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2003-01-10T21:21:21Z |  | encounters.csv |
| 2003-01-10 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-01-10 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2003-01-10 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2003-01-10 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-01-10 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2003-01-10 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2003-01-10 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=7; total cost=893.20 | **DIABETES** | medications.csv |
| 2003-01-10 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=7; total cost=1844.43 | **HYPERTENSION** | medications.csv |
| 2003-01-10 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=7; total cost=622.23 |  | medications.csv |
| 2003-01-10 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=7; total cost=5270.44 | **DIABETES** | medications.csv |
| 2003-01-10 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=7; total cost=386.82 |  | medications.csv |
| 2003-01-10 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=7; total cost=83.51 |  | medications.csv |
| 2003-08-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2003-08-08T21:21:21Z |  | encounters.csv |
| 2003-08-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-08-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2003-08-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2003-08-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-08-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2003-08-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2003-08-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=12.46 | **DIABETES** | medications.csv |
| 2003-08-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2003-08-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=79.50 |  | medications.csv |
| 2003-08-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=520.41 | **DIABETES** | medications.csv |
| 2003-08-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=3.76 |  | medications.csv |
| 2003-08-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=24.20 |  | medications.csv |
| 2003-09-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2003-09-26T21:21:21Z |  | encounters.csv |
| 2003-09-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-09-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2003-09-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2003-09-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-09-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2003-09-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2003-09-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=374.78 | **DIABETES** | medications.csv |
| 2003-09-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2003-09-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=124.24 |  | medications.csv |
| 2003-09-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=1605.42 | **DIABETES** | medications.csv |
| 2003-09-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=192.90 |  | medications.csv |
| 2003-09-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=356.20 |  | medications.csv |
| 2003-12-05 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2003-12-05T21:21:21Z |  | encounters.csv |
| 2003-12-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-12-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2003-12-05 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2003-12-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-12-05 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2003-12-05 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2003-12-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=491.23 | **DIABETES** | medications.csv |
| 2003-12-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2003-12-05 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=62.33 |  | medications.csv |
| 2003-12-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1092.69 | **DIABETES** | medications.csv |
| 2003-12-05 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=61.43 |  | medications.csv |
| 2003-12-05 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=209.10 |  | medications.csv |
| 2003-12-19 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2003-12-19T21:21:21Z |  | encounters.csv |
| 2003-12-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-12-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2003-12-19 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2003-12-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2003-12-19 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2003-12-19 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2003-12-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=492.19 | **DIABETES** | medications.csv |
| 2003-12-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2003-12-19 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=12.24 |  | medications.csv |
| 2003-12-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1402.09 | **DIABETES** | medications.csv |
| 2003-12-19 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=175.03 |  | medications.csv |
| 2003-12-19 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=45.26 |  | medications.csv |
| 2004-01-30 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-01-30T21:21:21Z |  | encounters.csv |
| 2004-01-30 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-01-30 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-01-30 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-01-30 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-01-30 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-01-30 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-01-30 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1467.03 | **DIABETES** | medications.csv |
| 2004-01-30 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2004-01-30 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=366.42 |  | medications.csv |
| 2004-01-30 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=3090.21 | **DIABETES** | medications.csv |
| 2004-01-30 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=363.93 |  | medications.csv |
| 2004-01-30 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=494.31 |  | medications.csv |
| 2004-04-30 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-04-30T21:21:21Z |  | encounters.csv |
| 2004-04-30 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-04-30 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-04-30 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-04-30 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-04-30 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-04-30 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-04-30 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=263.48 | **DIABETES** | medications.csv |
| 2004-04-30 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2004-04-30 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=44.64 |  | medications.csv |
| 2004-04-30 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=996.09 | **DIABETES** | medications.csv |
| 2004-04-30 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=87.99 |  | medications.csv |
| 2004-04-30 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=128.71 |  | medications.csv |
| 2004-05-28 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-05-28T21:21:21Z |  | encounters.csv |
| 2004-05-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-05-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-05-28 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-05-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-05-28 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-05-28 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-05-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=212.30 | **DIABETES** | medications.csv |
| 2004-05-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2004-05-28 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=50.18 |  | medications.csv |
| 2004-05-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1106.14 | **DIABETES** | medications.csv |
| 2004-05-28 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=96.74 |  | medications.csv |
| 2004-05-28 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=65.06 |  | medications.csv |
| 2004-06-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-06-25T21:21:21Z |  | encounters.csv |
| 2004-06-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-06-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-06-25 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-06-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-06-25 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-06-25 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-06-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=324.96 | **DIABETES** | medications.csv |
| 2004-06-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2004-06-25 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=55.20 |  | medications.csv |
| 2004-06-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1110.66 | **DIABETES** | medications.csv |
| 2004-06-25 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=408.51 |  | medications.csv |
| 2004-06-25 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=375.96 |  | medications.csv |
| 2004-09-24 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-09-24T21:21:21Z |  | encounters.csv |
| 2004-09-24 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-09-24 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-09-24 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-09-24 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-09-24 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-09-24 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-09-24 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=95.16 | **DIABETES** | medications.csv |
| 2004-09-24 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2004-09-24 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=105.14 |  | medications.csv |
| 2004-09-24 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=634.32 | **DIABETES** | medications.csv |
| 2004-09-24 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=250.93 |  | medications.csv |
| 2004-09-24 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=138.24 |  | medications.csv |
| 2004-10-29 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-10-29T21:21:21Z |  | encounters.csv |
| 2004-10-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-10-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-10-29 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-10-29 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-10-29 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-10-29 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-10-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=126.45 | **DIABETES** | medications.csv |
| 2004-10-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2004-10-29 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=37.47 |  | medications.csv |
| 2004-10-29 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1767.02 | **DIABETES** | medications.csv |
| 2004-10-29 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=140.43 |  | medications.csv |
| 2004-10-29 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=3.45 |  | medications.csv |
| 2004-11-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-11-26T21:21:21Z |  | encounters.csv |
| 2004-11-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-11-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-11-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-11-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-11-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-11-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-11-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=43.81 | **DIABETES** | medications.csv |
| 2004-11-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2004-11-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=37.61 |  | medications.csv |
| 2004-11-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=921.52 | **DIABETES** | medications.csv |
| 2004-11-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=63.34 |  | medications.csv |
| 2004-11-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=130.64 |  | medications.csv |
| 2004-12-24 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2004-12-24T21:21:21Z |  | encounters.csv |
| 2004-12-24 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-12-24 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-12-24 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-12-24 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-12-24 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-12-24 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-12-24 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=48.82 | **DIABETES** | medications.csv |
| 2004-12-24 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2004-12-24 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=63.16 |  | medications.csv |
| 2004-12-24 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=592.20 | **DIABETES** | medications.csv |
| 2004-12-24 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=125.18 |  | medications.csv |
| 2004-12-24 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=82.80 |  | medications.csv |
| 2004-12-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2004-12-31T21:21:21Z |  | encounters.csv |
| 2004-12-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-12-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2004-12-31 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2004-12-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2004-12-31 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2004-12-31 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2004-12-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=478.44 | **DIABETES** | medications.csv |
| 2004-12-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2004-12-31 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=58.16 |  | medications.csv |
| 2004-12-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1435.81 | **DIABETES** | medications.csv |
| 2004-12-31 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=124.28 |  | medications.csv |
| 2004-12-31 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=14.03 |  | medications.csv |
| 2005-01-21 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-01-21T21:21:21Z |  | encounters.csv |
| 2005-01-21 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-01-21 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-01-21 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-01-21 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-01-21 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-01-21 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-01-21 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=205.44 | **DIABETES** | medications.csv |
| 2005-01-21 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2005-01-21 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=276.60 |  | medications.csv |
| 2005-01-21 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=2768.76 | **DIABETES** | medications.csv |
| 2005-01-21 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=790.88 |  | medications.csv |
| 2005-01-21 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=76.24 |  | medications.csv |
| 2005-05-27 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-05-27T21:21:21Z |  | encounters.csv |
| 2005-05-27 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-05-27 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-05-27 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-05-27 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-05-27 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-05-27 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-05-27 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=233.96 | **DIABETES** | medications.csv |
| 2005-05-27 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2005-05-27 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=138.68 |  | medications.csv |
| 2005-05-27 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=399.05 | **DIABETES** | medications.csv |
| 2005-05-27 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=66.20 |  | medications.csv |
| 2005-05-27 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=43.66 |  | medications.csv |
| 2005-06-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-06-17T21:21:21Z |  | encounters.csv |
| 2005-06-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-06-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-06-17 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-06-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-06-17 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-06-17 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-06-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=142.28 | **DIABETES** | medications.csv |
| 2005-06-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2005-06-17 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=45.18 |  | medications.csv |
| 2005-06-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=543.23 | **DIABETES** | medications.csv |
| 2005-06-17 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=34.09 |  | medications.csv |
| 2005-06-17 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=91.15 |  | medications.csv |
| 2005-07-22 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-07-22T21:21:21Z |  | encounters.csv |
| 2005-07-22 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-07-22 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-07-22 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-07-22 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-07-22 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-07-22 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-07-22 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=274.45 | **DIABETES** | medications.csv |
| 2005-07-22 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2005-07-22 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=43.21 |  | medications.csv |
| 2005-07-22 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1234.89 | **DIABETES** | medications.csv |
| 2005-07-22 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=223.02 |  | medications.csv |
| 2005-07-22 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=75.80 |  | medications.csv |
| 2005-08-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-08-19T21:21:21Z |  | encounters.csv |
| 2005-08-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-08-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-08-19 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-08-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-08-19 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-08-19 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-08-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=599.16 | **DIABETES** | medications.csv |
| 2005-08-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2005-08-19 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=62.94 |  | medications.csv |
| 2005-08-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=2092.18 | **DIABETES** | medications.csv |
| 2005-08-19 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=516.96 |  | medications.csv |
| 2005-08-19 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=96.38 |  | medications.csv |
| 2005-10-21 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-10-21T21:21:21Z |  | encounters.csv |
| 2005-10-21 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-10-21 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-10-21 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-10-21 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-10-21 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-10-21 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-10-21 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=91.12 | **DIABETES** | medications.csv |
| 2005-10-21 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2005-10-21 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=49.42 |  | medications.csv |
| 2005-10-21 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=716.96 | **DIABETES** | medications.csv |
| 2005-10-21 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=21.31 |  | medications.csv |
| 2005-10-21 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=20.76 |  | medications.csv |
| 2005-11-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-11-25T21:21:21Z |  | encounters.csv |
| 2005-11-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-11-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-11-25 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-11-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-11-25 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-11-25 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-11-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=239.84 | **DIABETES** | medications.csv |
| 2005-11-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2005-11-25 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=144.15 |  | medications.csv |
| 2005-11-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1360.37 | **DIABETES** | medications.csv |
| 2005-11-25 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=99.99 |  | medications.csv |
| 2005-11-25 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=18.31 |  | medications.csv |
| 2005-12-16 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2005-12-16T21:21:21Z |  | encounters.csv |
| 2005-12-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-12-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-12-16 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-12-16 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-12-16 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-12-16 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-12-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=80.94 | **DIABETES** | medications.csv |
| 2005-12-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2005-12-16 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=87.78 |  | medications.csv |
| 2005-12-16 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=473.33 | **DIABETES** | medications.csv |
| 2005-12-16 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=44.60 |  | medications.csv |
| 2005-12-16 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=121.67 |  | medications.csv |
| 2005-12-30 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2005-12-30T21:21:21Z |  | encounters.csv |
| 2005-12-30 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-12-30 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2005-12-30 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2005-12-30 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2005-12-30 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2005-12-30 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2005-12-30 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=190.87 | **DIABETES** | medications.csv |
| 2005-12-30 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2005-12-30 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=47.02 |  | medications.csv |
| 2005-12-30 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=384.00 | **DIABETES** | medications.csv |
| 2005-12-30 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=170.58 |  | medications.csv |
| 2005-12-30 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=133.34 |  | medications.csv |
| 2006-01-20 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2006-01-20T21:21:21Z |  | encounters.csv |
| 2006-01-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-01-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2006-01-20 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2006-01-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-01-20 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2006-01-20 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2006-01-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=708.90 | **DIABETES** | medications.csv |
| 2006-01-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2006-01-20 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=431.61 |  | medications.csv |
| 2006-01-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=4230.21 | **DIABETES** | medications.csv |
| 2006-01-20 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=619.20 |  | medications.csv |
| 2006-01-20 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=94.89 |  | medications.csv |
| 2006-05-19 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2006-05-19T21:21:21Z |  | encounters.csv |
| 2006-05-19 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-05-19 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2006-05-19 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2006-05-19 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-05-19 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2006-05-19 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2006-05-19 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=975.63 | **DIABETES** | medications.csv |
| 2006-05-19 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2006-05-19 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=301.08 |  | medications.csv |
| 2006-05-19 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=771.12 | **DIABETES** | medications.csv |
| 2006-05-19 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=19.74 |  | medications.csv |
| 2006-05-19 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=360.57 |  | medications.csv |
| 2006-08-18 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2006-08-18T21:21:21Z |  | encounters.csv |
| 2006-08-18 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-08-18 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2006-08-18 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2006-08-18 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-08-18 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2006-08-18 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2006-08-18 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=223.64 | **DIABETES** | medications.csv |
| 2006-08-18 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2006-08-18 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=84.86 |  | medications.csv |
| 2006-08-18 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=639.96 | **DIABETES** | medications.csv |
| 2006-08-18 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=191.15 |  | medications.csv |
| 2006-08-18 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=57.54 |  | medications.csv |
| 2006-09-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2006-09-08T21:21:21Z |  | encounters.csv |
| 2006-09-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-09-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2006-09-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2006-09-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-09-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2006-09-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2006-09-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=484.30 | **DIABETES** | medications.csv |
| 2006-09-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2006-09-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=221.68 |  | medications.csv |
| 2006-09-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=832.80 | **DIABETES** | medications.csv |
| 2006-09-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=333.74 |  | medications.csv |
| 2006-09-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=116.00 |  | medications.csv |
| 2006-11-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2006-11-17T21:21:21Z |  | encounters.csv |
| 2006-11-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-11-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2006-11-17 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2006-11-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2006-11-17 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2006-11-17 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2006-11-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=173.72 | **DIABETES** | medications.csv |
| 2006-11-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2006-11-17 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=44.34 |  | medications.csv |
| 2006-11-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1140.48 | **DIABETES** | medications.csv |
| 2006-11-17 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=63.08 |  | medications.csv |
| 2006-11-17 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=112.83 |  | medications.csv |
| 2007-01-05 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2007-01-05T21:21:21Z |  | encounters.csv |
| 2007-01-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-01-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-01-05 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-01-05 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-05 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=270.71 | **DIABETES** | medications.csv |
| 2007-01-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-01-05 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=77.58 |  | medications.csv |
| 2007-01-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1061.39 | **DIABETES** | medications.csv |
| 2007-01-05 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=96.91 |  | medications.csv |
| 2007-01-05 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=146.63 |  | medications.csv |
| 2007-01-10 20:51:21 | Encounters | Encounter for symptom; class=ambulatory; reason=Acute bronchitis (disorder); end=2007-01-10T21:06:21Z |  | encounters.csv |
| 2007-01-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-01-12T21:21:21Z |  | encounters.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=286.55 | **DIABETES** | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=386.60 | **DIABETES** | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=29.25 |  | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=62.26 |  | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1147.05 | **DIABETES** | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=1276.16 | **DIABETES** | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=219.77 |  | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=96.40 |  | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=170.45 |  | medications.csv |
| 2007-01-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=46.78 |  | medications.csv |
| 2007-04-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-04-06T21:21:21Z |  | encounters.csv |
| 2007-04-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-04-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-04-06 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-04-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-04-06 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-04-06 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-04-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=430.61 | **DIABETES** | medications.csv |
| 2007-04-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-04-06 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=45.93 |  | medications.csv |
| 2007-04-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=432.01 | **DIABETES** | medications.csv |
| 2007-04-06 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=40.96 |  | medications.csv |
| 2007-04-06 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=119.06 |  | medications.csv |
| 2007-05-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-05-25T21:21:21Z |  | encounters.csv |
| 2007-05-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-05-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-05-25 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-05-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-05-25 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-05-25 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-05-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=304.87 | **DIABETES** | medications.csv |
| 2007-05-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-05-25 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=62.82 |  | medications.csv |
| 2007-05-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1225.29 | **DIABETES** | medications.csv |
| 2007-05-25 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=126.65 |  | medications.csv |
| 2007-05-25 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=78.85 |  | medications.csv |
| 2007-07-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-07-06T21:21:21Z |  | encounters.csv |
| 2007-07-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-07-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-07-06 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-07-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-07-06 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-07-06 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-07-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=265.64 | **DIABETES** | medications.csv |
| 2007-07-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2007-07-06 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=207.44 |  | medications.csv |
| 2007-07-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=1022.96 | **DIABETES** | medications.csv |
| 2007-07-06 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=145.76 |  | medications.csv |
| 2007-07-06 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=208.98 |  | medications.csv |
| 2007-09-07 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-09-07T21:21:21Z |  | encounters.csv |
| 2007-09-07 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-09-07 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-09-07 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-09-07 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-09-07 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-09-07 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-09-07 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=90.08 | **DIABETES** | medications.csv |
| 2007-09-07 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-09-07 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=77.12 |  | medications.csv |
| 2007-09-07 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=382.45 | **DIABETES** | medications.csv |
| 2007-09-07 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=27.92 |  | medications.csv |
| 2007-09-07 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=89.10 |  | medications.csv |
| 2007-10-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-10-12T21:21:21Z |  | encounters.csv |
| 2007-10-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-10-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-10-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-10-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-10-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-10-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-10-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=455.31 | **DIABETES** | medications.csv |
| 2007-10-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-10-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=39.20 |  | medications.csv |
| 2007-10-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=533.34 | **DIABETES** | medications.csv |
| 2007-10-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=114.36 |  | medications.csv |
| 2007-10-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=133.00 |  | medications.csv |
| 2007-11-09 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-11-09T21:21:21Z |  | encounters.csv |
| 2007-11-09 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-11-09 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-11-09 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-11-09 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-11-09 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-11-09 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-11-09 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=350.78 | **DIABETES** | medications.csv |
| 2007-11-09 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-11-09 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=53.55 |  | medications.csv |
| 2007-11-09 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=512.69 | **DIABETES** | medications.csv |
| 2007-11-09 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=83.09 |  | medications.csv |
| 2007-11-09 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=83.07 |  | medications.csv |
| 2007-12-07 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2007-12-07T21:21:21Z |  | encounters.csv |
| 2007-12-07 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-12-07 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2007-12-07 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2007-12-07 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2007-12-07 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2007-12-07 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2007-12-07 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=188.23 | **DIABETES** | medications.csv |
| 2007-12-07 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2007-12-07 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=137.20 |  | medications.csv |
| 2007-12-07 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=400.96 | **DIABETES** | medications.csv |
| 2007-12-07 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=111.78 |  | medications.csv |
| 2007-12-07 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=40.19 |  | medications.csv |
| 2008-01-11 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2008-01-11T21:36:21Z |  | encounters.csv |
| 2008-01-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-01-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2008-01-11 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2008-01-11 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-01-11 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2008-01-11 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2008-01-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=368.06 | **DIABETES** | medications.csv |
| 2008-01-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2008-01-11 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=125.94 |  | medications.csv |
| 2008-01-11 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=624.68 | **DIABETES** | medications.csv |
| 2008-01-11 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=185.73 |  | medications.csv |
| 2008-01-11 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=22.75 |  | medications.csv |
| 2008-01-18 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2008-01-18T21:21:21Z |  | encounters.csv |
| 2008-01-18 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-01-18 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2008-01-18 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2008-01-18 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-01-18 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2008-01-18 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2008-01-18 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=26.90 | **DIABETES** | medications.csv |
| 2008-01-18 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2008-01-18 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=55.37 |  | medications.csv |
| 2008-01-18 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=842.71 | **DIABETES** | medications.csv |
| 2008-01-18 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=58.23 |  | medications.csv |
| 2008-01-18 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=92.53 |  | medications.csv |
| 2008-02-01 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2008-02-01T21:21:21Z |  | encounters.csv |
| 2008-02-01 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-02-01 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2008-02-01 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2008-02-01 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-02-01 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2008-02-01 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2008-02-01 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=79.08 | **DIABETES** | medications.csv |
| 2008-02-01 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2008-02-01 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=17.42 |  | medications.csv |
| 2008-02-01 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1101.65 | **DIABETES** | medications.csv |
| 2008-02-01 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=70.98 |  | medications.csv |
| 2008-02-01 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=135.29 |  | medications.csv |
| 2008-03-07 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2008-03-07T21:21:21Z |  | encounters.csv |
| 2008-03-07 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-03-07 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2008-03-07 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2008-03-07 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-03-07 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2008-03-07 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2008-03-07 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=216.72 | **DIABETES** | medications.csv |
| 2008-03-07 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2008-03-07 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=297.69 |  | medications.csv |
| 2008-03-07 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=2316.36 | **DIABETES** | medications.csv |
| 2008-03-07 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=203.76 |  | medications.csv |
| 2008-03-07 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=511.89 |  | medications.csv |
| 2008-07-04 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2008-07-04T21:21:21Z |  | encounters.csv |
| 2008-07-04 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-07-04 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2008-07-04 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2008-07-04 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-07-04 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2008-07-04 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2008-07-04 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=774.93 | **DIABETES** | medications.csv |
| 2008-07-04 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2008-07-04 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=149.61 |  | medications.csv |
| 2008-07-04 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1989.48 | **DIABETES** | medications.csv |
| 2008-07-04 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=355.80 |  | medications.csv |
| 2008-07-04 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=242.31 |  | medications.csv |
| 2008-10-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2008-10-31T21:21:21Z |  | encounters.csv |
| 2008-10-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-10-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2008-10-31 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2008-10-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-10-31 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2008-10-31 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2008-10-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=179.38 | **DIABETES** | medications.csv |
| 2008-10-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2008-10-31 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=74.51 |  | medications.csv |
| 2008-10-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1196.82 | **DIABETES** | medications.csv |
| 2008-10-31 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=191.65 |  | medications.csv |
| 2008-10-31 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=130.91 |  | medications.csv |
| 2008-12-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2008-12-12T21:21:21Z |  | encounters.csv |
| 2008-12-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-12-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2008-12-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2008-12-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2008-12-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2008-12-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2008-12-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=568.66 | **DIABETES** | medications.csv |
| 2008-12-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2008-12-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=69.03 |  | medications.csv |
| 2008-12-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=270.36 | **DIABETES** | medications.csv |
| 2008-12-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=44.21 |  | medications.csv |
| 2008-12-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=17.86 |  | medications.csv |
| 2009-01-16 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2009-01-16T21:21:21Z |  | encounters.csv |
| 2009-01-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-01-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-01-16 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2009-01-16 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-01-16 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2009-01-16 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2009-01-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=67.47 | **DIABETES** | medications.csv |
| 2009-01-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2009-01-16 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=56.72 |  | medications.csv |
| 2009-01-16 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=450.67 | **DIABETES** | medications.csv |
| 2009-01-16 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=147.84 |  | medications.csv |
| 2009-01-16 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=31.14 |  | medications.csv |
| 2009-02-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2009-02-06T21:21:21Z |  | encounters.csv |
| 2009-02-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-02-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-02-06 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2009-02-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-02-06 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2009-02-06 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2009-02-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=182.68 | **DIABETES** | medications.csv |
| 2009-02-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2009-02-06 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=288.36 |  | medications.csv |
| 2009-02-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=7052.56 | **DIABETES** | medications.csv |
| 2009-02-06 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=298.28 |  | medications.csv |
| 2009-02-06 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=264.88 |  | medications.csv |
| 2009-05-01 00:00:00 | Diagnoses | Coronary Heart Disease code=53741008 |  | conditions.csv |
| 2009-05-01 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2009-05-01T21:06:21Z |  | encounters.csv |
| 2009-05-01 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=65.00 | **HYPERTENSION** | medications.csv |
| 2009-05-01 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=184.16 |  | medications.csv |
| 2009-05-01 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=180.36 |  | medications.csv |
| 2009-05-01 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=48.86 |  | medications.csv |
| 2009-07-03 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2009-07-03T21:21:21Z |  | encounters.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=213.48 | **DIABETES** | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=32.59 | **HYPERTENSION** | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=43.22 |  | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=54.96 |  | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=319.54 | **DIABETES** | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=240.26 |  | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=23.99 |  | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=263.78 |  | medications.csv |
| 2009-07-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=104.46 |  | medications.csv |
| 2009-07-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2009-07-31T21:21:21Z |  | encounters.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=400.59 | **DIABETES** | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=64.65 | **HYPERTENSION** | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=29.17 |  | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=107.59 |  | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=602.47 | **DIABETES** | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=39.52 |  | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=26.04 |  | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=224.84 |  | medications.csv |
| 2009-07-31 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=59.08 |  | medications.csv |
| 2009-09-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2009-09-25T21:21:21Z |  | encounters.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=128.30 | **DIABETES** | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=141.50 | **HYPERTENSION** | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=232.58 |  | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=160.76 |  | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=1200.18 | **DIABETES** | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=274.06 |  | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=14.72 |  | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=269.46 |  | medications.csv |
| 2009-09-25 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=297.74 |  | medications.csv |
| 2009-12-04 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2009-12-04T21:21:21Z |  | encounters.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=214.00 | **DIABETES** | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=12.86 | **HYPERTENSION** | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=38.67 |  | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=110.99 |  | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=580.61 | **DIABETES** | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=141.26 |  | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=24.49 |  | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=202.34 |  | medications.csv |
| 2009-12-04 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=122.83 |  | medications.csv |
| 2010-01-01 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2010-01-01T21:21:21Z |  | encounters.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=87.05 | **DIABETES** | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=36.85 | **HYPERTENSION** | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=140.51 |  | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=49.75 |  | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=468.77 | **DIABETES** | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=45.21 |  | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=25.38 |  | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=177.18 |  | medications.csv |
| 2010-01-01 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=129.65 |  | medications.csv |
| 2010-01-22 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2010-01-22T21:21:21Z |  | encounters.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=394.61 | **DIABETES** | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=21.48 | **HYPERTENSION** | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=93.83 |  | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=46.13 |  | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=437.42 | **DIABETES** | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=64.34 |  | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=21.89 |  | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=99.59 |  | medications.csv |
| 2010-01-22 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=14.93 |  | medications.csv |
| 2010-01-29 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2010-01-29T21:21:21Z |  | encounters.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=39.79 | **DIABETES** | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=30.14 | **HYPERTENSION** | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=31.14 |  | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=23.19 |  | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=261.05 | **DIABETES** | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=38.66 |  | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=18.60 |  | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=107.97 |  | medications.csv |
| 2010-01-29 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=15.82 |  | medications.csv |
| 2010-02-14 20:51:21 | Lab Results | DALY: 26.0 a; type=numeric |  | observations.csv |
| 2010-02-14 20:51:21 | Lab Results | QALY: 42.0 a; type=numeric |  | observations.csv |
| 2010-02-14 20:51:21 | Lab Results | QOLS: 0.4 {score}; type=numeric |  | observations.csv |
| 2010-02-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2010-02-26T21:21:21Z |  | encounters.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=409.82 | **DIABETES** | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=50.43 | **HYPERTENSION** | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=30.86 |  | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=51.12 |  | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=691.76 | **DIABETES** | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=329.52 |  | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=14.03 |  | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=72.75 |  | medications.csv |
| 2010-02-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=50.11 |  | medications.csv |
| 2010-03-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2010-03-26T21:21:21Z |  | encounters.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=890.32 | **DIABETES** | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=32.58 | **HYPERTENSION** | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=124.18 |  | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=178.90 |  | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=2215.66 | **DIABETES** | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=283.54 |  | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=10.36 |  | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=228.00 |  | medications.csv |
| 2010-03-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=137.84 |  | medications.csv |
| 2010-05-21 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-05-21T21:06:21Z |  | encounters.csv |
| 2010-05-28 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2010-05-28T21:21:21Z |  | encounters.csv |
| 2010-05-28 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Body Mass Index: 47.4 kg/m2; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Body Weight: 127.3 kg; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Calcium: 10.1 mg/dL; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Carbon Dioxide: 26.3 mmol/L; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Chloride: 109.4 mmol/L; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Creatinine: 6.0 mg/dL; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Diastolic Blood Pressure: 117.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 17.7 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Glucose: 105.1 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Heart rate: 66.0 /min; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.4 %; type=numeric | **DIABETES** | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 46.4 mg/dL; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 141.9 mg/dL; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 57.7 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Potassium: 5.0 mmol/L; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Sodium: 141.1 mmol/L; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Systolic Blood Pressure: 155.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Total Cholesterol: 226.4 mg/dL; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Triglycerides: 190.7 mg/dL; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Lab Results | Urea Nitrogen: 14.2 mg/dL; type=numeric |  | observations.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=232.16 | **DIABETES** | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=31.29 | **HYPERTENSION** | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=31.03 |  | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=71.27 |  | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=404.81 | **DIABETES** | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=173.95 |  | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=17.22 |  | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=11.23 |  | medications.csv |
| 2010-05-28 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=71.55 |  | medications.csv |
| 2010-06-25 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-06-25T21:06:21Z |  | encounters.csv |
| 2010-07-02 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2010-07-02T21:21:21Z |  | encounters.csv |
| 2010-07-02 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Body Mass Index: 47.5 kg/m2; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Body Weight: 127.5 kg; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Calcium: 8.8 mg/dL; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Carbon Dioxide: 25.0 mmol/L; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Chloride: 101.4 mmol/L; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Creatinine: 4.5 mg/dL; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Diastolic Blood Pressure: 99.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.9 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Glucose: 100.6 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Heart rate: 71.0 /min; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.4 %; type=numeric | **DIABETES** | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 40.9 mg/dL; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 134.0 mg/dL; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 122.1 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Potassium: 4.4 mmol/L; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Sodium: 139.3 mmol/L; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Systolic Blood Pressure: 155.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Total Cholesterol: 209.8 mg/dL; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Triglycerides: 174.8 mg/dL; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Lab Results | Urea Nitrogen: 15.1 mg/dL; type=numeric |  | observations.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=507.83 | **DIABETES** | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=91.11 | **HYPERTENSION** | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=143.45 |  | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=54.65 |  | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=326.56 | **DIABETES** | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=49.80 |  | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=38.15 |  | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=84.63 |  | medications.csv |
| 2010-07-02 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=62.32 |  | medications.csv |
| 2010-07-23 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-07-23T21:06:21Z |  | encounters.csv |
| 2010-08-20 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-08-20T21:06:21Z |  | encounters.csv |
| 2010-08-27 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2010-08-27T21:21:21Z |  | encounters.csv |
| 2010-08-27 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Body Mass Index: 47.7 kg/m2; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Body Weight: 127.9 kg; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Calcium: 9.8 mg/dL; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Carbon Dioxide: 23.5 mmol/L; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Chloride: 108.0 mmol/L; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Creatinine: 4.8 mg/dL; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Diastolic Blood Pressure: 97.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 22.3 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Glucose: 119.3 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Heart rate: 61.0 /min; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.4 %; type=numeric | **DIABETES** | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 40.4 mg/dL; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 137.1 mg/dL; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 271.7 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Potassium: 3.9 mmol/L; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Sodium: 143.5 mmol/L; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Systolic Blood Pressure: 175.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Total Cholesterol: 210.2 mg/dL; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Triglycerides: 163.3 mg/dL; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Lab Results | Urea Nitrogen: 20.0 mg/dL; type=numeric |  | observations.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=1047.12 | **DIABETES** | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=4; total cost=119.44 | **HYPERTENSION** | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=4; total cost=210.88 |  | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=447.60 |  | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=1143.64 | **DIABETES** | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=4; total cost=68.04 |  | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=4; total cost=121.00 |  | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=554.08 |  | medications.csv |
| 2010-08-27 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=18.64 |  | medications.csv |
| 2010-09-17 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-09-17T21:06:21Z |  | encounters.csv |
| 2010-10-22 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-10-22T21:06:21Z |  | encounters.csv |
| 2010-12-16 00:00:00 | Diagnoses | Acute viral pharyngitis (disorder) code=195662009; recorded stop=2010-12-28 |  | conditions.csv |
| 2010-12-16 20:51:21 | Encounters | Encounter for symptom; class=ambulatory; reason=Acute viral pharyngitis (disorder); end=2010-12-16T21:06:21Z |  | encounters.csv |
| 2010-12-16 20:51:21 | Lab Results | Body temperature: 37.8 Cel; type=numeric |  | observations.csv |
| 2010-12-24 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-12-24T21:06:21Z |  | encounters.csv |
| 2010-12-31 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2010-12-31T21:06:21Z |  | encounters.csv |
| 2011-01-21 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2011-01-21T21:21:21Z |  | encounters.csv |
| 2011-01-21 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Body Mass Index: 48.1 kg/m2; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Body Weight: 129.0 kg; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Calcium: 8.9 mg/dL; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Carbon Dioxide: 20.8 mmol/L; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Chloride: 105.5 mmol/L; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Creatinine: 4.4 mg/dL; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Diastolic Blood Pressure: 108.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 24.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Glucose: 109.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Heart rate: 66.0 /min; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 55.3 mg/dL; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 128.1 mg/dL; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 286.4 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Potassium: 4.0 mmol/L; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Sodium: 140.1 mmol/L; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Systolic Blood Pressure: 160.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Total Cholesterol: 218.6 mg/dL; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Triglycerides: 175.9 mg/dL; type=numeric |  | observations.csv |
| 2011-01-21 20:51:21 | Lab Results | Urea Nitrogen: 9.2 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=112.38 | **DIABETES** | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=11.59 | **HYPERTENSION** | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=81.50 |  | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=71.48 |  | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=514.82 | **DIABETES** | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=321.62 |  | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=15.91 |  | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=102.11 |  | medications.csv |
| 2011-01-21 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=145.07 |  | medications.csv |
| 2011-01-28 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2011-01-28T21:36:21Z |  | encounters.csv |
| 2011-01-28 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Body Mass Index: 48.1 kg/m2; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Body Weight: 129.0 kg; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Calcium: 9.8 mg/dL; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Carbon Dioxide: 28.8 mmol/L; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Chloride: 106.8 mmol/L; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Creatinine: 6.3 mg/dL; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Diastolic Blood Pressure: 108.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 17.1 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Glucose: 110.7 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Heart rate: 71.0 /min; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 44.9 mg/dL; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 124.8 mg/dL; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 128.3 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 0.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Potassium: 5.0 mmol/L; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Sodium: 141.6 mmol/L; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Systolic Blood Pressure: 163.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Total Cholesterol: 205.3 mg/dL; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Triglycerides: 177.8 mg/dL; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Lab Results | Urea Nitrogen: 11.7 mg/dL; type=numeric |  | observations.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=194.60 | **DIABETES** | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=30.93 | **HYPERTENSION** | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=41.70 |  | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=145.19 |  | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1087.67 | **DIABETES** | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=173.88 |  | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=24.23 |  | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=55.68 |  | medications.csv |
| 2011-01-28 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=99.20 |  | medications.csv |
| 2011-02-14 20:51:21 | Lab Results | DALY: 26.6 a; type=numeric |  | observations.csv |
| 2011-02-14 20:51:21 | Lab Results | QALY: 42.4 a; type=numeric |  | observations.csv |
| 2011-02-14 20:51:21 | Lab Results | QOLS: 0.4 {score}; type=numeric |  | observations.csv |
| 2011-02-18 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-02-18T21:06:21Z |  | encounters.csv |
| 2011-02-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2011-02-25T21:21:21Z |  | encounters.csv |
| 2011-02-25 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Body Mass Index: 48.2 kg/m2; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Body Weight: 129.2 kg; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Calcium: 8.7 mg/dL; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Carbon Dioxide: 26.5 mmol/L; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Chloride: 106.4 mmol/L; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Creatinine: 4.3 mg/dL; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Diastolic Blood Pressure: 99.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 24.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Glucose: 118.2 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Heart rate: 87.0 /min; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 57.9 mg/dL; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 113.8 mg/dL; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 295.3 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 0.0 {score}; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Potassium: 4.1 mmol/L; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Respiratory rate: 12.0 /min; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Sodium: 138.3 mmol/L; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Systolic Blood Pressure: 158.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Total Cholesterol: 202.5 mg/dL; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Triglycerides: 154.2 mg/dL; type=numeric |  | observations.csv |
| 2011-02-25 20:51:21 | Lab Results | Urea Nitrogen: 18.1 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=1802.36 | **DIABETES** | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=4; total cost=201.44 | **HYPERTENSION** | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=4; total cost=202.88 |  | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=229.00 |  | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=397.24 | **DIABETES** | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=4; total cost=1288.04 |  | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=4; total cost=68.20 |  | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=889.20 |  | medications.csv |
| 2011-02-25 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=204.08 |  | medications.csv |
| 2011-03-18 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-03-18T21:06:21Z |  | encounters.csv |
| 2011-04-15 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-04-15T21:06:21Z |  | encounters.csv |
| 2011-05-20 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-05-20T21:06:21Z |  | encounters.csv |
| 2011-07-15 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2011-07-15T21:21:21Z |  | encounters.csv |
| 2011-07-15 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Carbon Dioxide: 28.5 mmol/L; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Chloride: 104.9 mmol/L; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Creatinine: 6.7 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Diastolic Blood Pressure: 96.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.0 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Glucose: 107.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Heart rate: 70.0 /min; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 44.2 mg/dL; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 137.7 mg/dL; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 248.2 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Potassium: 3.9 mmol/L; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Sodium: 142.5 mmol/L; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Systolic Blood Pressure: 183.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Total Cholesterol: 219.3 mg/dL; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Triglycerides: 187.0 mg/dL; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Lab Results | Urea Nitrogen: 18.0 mg/dL; type=numeric |  | observations.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=277.84 | **DIABETES** | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=23.28 | **HYPERTENSION** | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=17.96 |  | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=29.87 |  | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=311.33 | **DIABETES** | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=35.68 |  | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=13.19 |  | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=17.61 |  | medications.csv |
| 2011-07-15 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=115.99 |  | medications.csv |
| 2011-08-19 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-08-19T21:06:21Z |  | encounters.csv |
| 2011-08-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2011-08-26T21:21:21Z |  | encounters.csv |
| 2011-08-26 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Body Mass Index: 48.1 kg/m2; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Body Weight: 129.0 kg; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Calcium: 10.2 mg/dL; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Carbon Dioxide: 23.9 mmol/L; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Chloride: 109.5 mmol/L; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Creatinine: 5.9 mg/dL; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Diastolic Blood Pressure: 106.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 18.2 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Glucose: 104.3 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Heart rate: 66.0 /min; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 50.7 mg/dL; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 122.3 mg/dL; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 268.8 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Potassium: 4.0 mmol/L; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Sodium: 141.9 mmol/L; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Systolic Blood Pressure: 154.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Total Cholesterol: 211.4 mg/dL; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Triglycerides: 192.0 mg/dL; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Lab Results | Urea Nitrogen: 10.0 mg/dL; type=numeric |  | observations.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=173.36 | **DIABETES** | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=65.85 | **HYPERTENSION** | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=60.33 |  | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=20.01 |  | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1055.14 | **DIABETES** | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=297.06 |  | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=11.90 |  | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=52.55 |  | medications.csv |
| 2011-08-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=9.08 |  | medications.csv |
| 2011-09-16 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-09-16T21:06:21Z |  | encounters.csv |
| 2011-09-23 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2011-09-23T21:21:21Z |  | encounters.csv |
| 2011-09-23 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Body Mass Index: 47.7 kg/m2; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Body Weight: 128.1 kg; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Calcium: 9.1 mg/dL; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Carbon Dioxide: 28.4 mmol/L; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Chloride: 105.2 mmol/L; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Creatinine: 4.0 mg/dL; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Diastolic Blood Pressure: 106.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 26.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Glucose: 121.2 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Heart rate: 94.0 /min; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 48.6 mg/dL; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 137.2 mg/dL; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 106.0 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Potassium: 4.9 mmol/L; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Sodium: 140.5 mmol/L; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Systolic Blood Pressure: 177.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Total Cholesterol: 223.1 mg/dL; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Triglycerides: 186.6 mg/dL; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Lab Results | Urea Nitrogen: 11.9 mg/dL; type=numeric |  | observations.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=93.61 | **DIABETES** | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=42.53 | **HYPERTENSION** | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=90.65 |  | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=52.90 |  | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=409.65 | **DIABETES** | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=161.09 |  | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=23.48 |  | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=33.92 |  | medications.csv |
| 2011-09-23 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=48.18 |  | medications.csv |
| 2011-10-14 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-10-14T21:06:21Z |  | encounters.csv |
| 2011-10-21 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-10-21T21:06:21Z |  | encounters.csv |
| 2011-11-11 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-11-11T21:06:21Z |  | encounters.csv |
| 2011-11-18 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2011-11-18T21:21:21Z |  | encounters.csv |
| 2011-11-18 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Body Mass Index: 47.1 kg/m2; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Body Weight: 126.2 kg; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Calcium: 9.3 mg/dL; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Carbon Dioxide: 21.2 mmol/L; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Chloride: 106.9 mmol/L; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Creatinine: 4.0 mg/dL; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Diastolic Blood Pressure: 93.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 26.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Glucose: 116.8 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Heart rate: 88.0 /min; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.3 %; type=numeric | **DIABETES** | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 46.2 mg/dL; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 138.3 mg/dL; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 159.6 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Potassium: 4.1 mmol/L; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Respiratory rate: 12.0 /min; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Sodium: 143.0 mmol/L; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Systolic Blood Pressure: 165.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Total Cholesterol: 221.6 mg/dL; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Triglycerides: 185.8 mg/dL; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Lab Results | Urea Nitrogen: 9.7 mg/dL; type=numeric |  | observations.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=421.26 | **DIABETES** | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=23.32 | **HYPERTENSION** | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=184.68 |  | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=272.02 |  | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=267.36 | **DIABETES** | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=506.42 |  | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=48.40 |  | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=524.54 |  | medications.csv |
| 2011-11-18 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=159.36 |  | medications.csv |
| 2011-12-13 00:00:00 | Diagnoses | Acute bronchitis (disorder) code=10509002; recorded stop=2011-12-20 |  | conditions.csv |
| 2011-12-13 20:51:21 | Encounters | Encounter for symptom; class=ambulatory; reason=Acute bronchitis (disorder); end=2011-12-13T21:28:21Z |  | encounters.csv |
| 2011-12-13 20:51:21 | Medications Started | Acetaminophen 325 MG Oral Tablet code=313782; reason=Acute bronchitis (disorder); dispenses=1; total cost=7.19 |  | medications.csv |
| 2011-12-16 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2011-12-16T21:06:21Z |  | encounters.csv |
| 2011-12-20 20:51:21 | Medication Changes | Stopped/ended: Acetaminophen 325 MG Oral Tablet code=313782; reason=Acute bronchitis (disorder) | **MEDICATION CHANGE** | medications.csv |
| 2011-12-23 20:51:21 | Encounters | Emergency Encounter; class=emergency; end=2011-12-23T22:06:21Z |  | encounters.csv |
| 2012-02-03 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2012-02-03T21:36:21Z |  | encounters.csv |
| 2012-02-03 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Body Mass Index: 46.1 kg/m2; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Body Weight: 123.7 kg; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Carbon Dioxide: 21.3 mmol/L; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Chloride: 107.2 mmol/L; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Creatinine: 4.2 mg/dL; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Diastolic Blood Pressure: 112.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 24.2 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Glucose: 117.7 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Heart rate: 98.0 /min; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.1 %; type=numeric | **DIABETES** | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 49.3 mg/dL; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 118.1 mg/dL; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 93.0 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Potassium: 4.7 mmol/L; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Sodium: 141.4 mmol/L; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Systolic Blood Pressure: 171.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Total Cholesterol: 202.2 mg/dL; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Triglycerides: 173.9 mg/dL; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Lab Results | Urea Nitrogen: 11.2 mg/dL; type=numeric |  | observations.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=18.15 | **DIABETES** | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=34.38 | **HYPERTENSION** | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=26.80 |  | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=47.84 |  | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1311.91 | **DIABETES** | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=57.09 |  | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=27.99 |  | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=138.04 |  | medications.csv |
| 2012-02-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=31.64 |  | medications.csv |
| 2012-02-10 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-02-10T21:06:21Z |  | encounters.csv |
| 2012-02-14 20:51:21 | Lab Results | DALY: 27.2 a; type=numeric |  | observations.csv |
| 2012-02-14 20:51:21 | Lab Results | QALY: 42.8 a; type=numeric |  | observations.csv |
| 2012-02-14 20:51:21 | Lab Results | QOLS: 0.4 {score}; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2012-02-17T21:21:21Z |  | encounters.csv |
| 2012-02-17 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Body Mass Index: 45.9 kg/m2; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Body Weight: 123.2 kg; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Calcium: 8.8 mg/dL; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Carbon Dioxide: 25.3 mmol/L; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Chloride: 103.5 mmol/L; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Creatinine: 4.5 mg/dL; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Diastolic Blood Pressure: 107.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 22.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Glucose: 119.8 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Heart rate: 83.0 /min; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.0 %; type=numeric | **DIABETES** | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 41.0 mg/dL; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 143.3 mg/dL; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 293.7 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 0.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Potassium: 4.8 mmol/L; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Sodium: 140.9 mmol/L; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Systolic Blood Pressure: 187.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Total Cholesterol: 219.0 mg/dL; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Triglycerides: 173.8 mg/dL; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Lab Results | Urea Nitrogen: 12.0 mg/dL; type=numeric |  | observations.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=177.69 | **DIABETES** | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=3; total cost=31.14 | **HYPERTENSION** | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=3; total cost=258.36 |  | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=125.04 |  | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1031.55 | **DIABETES** | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=3; total cost=46.14 |  | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=3; total cost=50.55 |  | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=630.27 |  | medications.csv |
| 2012-02-17 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=420.87 |  | medications.csv |
| 2012-03-16 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-03-16T21:06:21Z |  | encounters.csv |
| 2012-05-11 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-05-11T21:06:21Z |  | encounters.csv |
| 2012-06-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2012-06-08T21:21:21Z |  | encounters.csv |
| 2012-06-08 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Body Mass Index: 44.5 kg/m2; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Body Weight: 119.5 kg; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Calcium: 9.9 mg/dL; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Carbon Dioxide: 24.7 mmol/L; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Chloride: 110.3 mmol/L; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Creatinine: 6.1 mg/dL; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Diastolic Blood Pressure: 98.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.1 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Glucose: 120.7 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Heart rate: 84.0 /min; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.7 %; type=numeric | **DIABETES** | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 55.4 mg/dL; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 127.5 mg/dL; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 234.4 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Potassium: 4.7 mmol/L; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Sodium: 139.3 mmol/L; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Systolic Blood Pressure: 160.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Total Cholesterol: 218.8 mg/dL; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Triglycerides: 179.4 mg/dL; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Lab Results | Urea Nitrogen: 13.7 mg/dL; type=numeric |  | observations.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=86.13 | **DIABETES** | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=17.53 | **HYPERTENSION** | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=136.96 |  | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=137.06 |  | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1378.23 | **DIABETES** | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=135.28 |  | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=37.89 |  | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=26.46 |  | medications.csv |
| 2012-06-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=102.66 |  | medications.csv |
| 2012-07-13 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2012-07-13T21:21:21Z |  | encounters.csv |
| 2012-07-13 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Body Mass Index: 44.1 kg/m2; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Body Weight: 118.3 kg; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Calcium: 10.2 mg/dL; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Carbon Dioxide: 24.4 mmol/L; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Chloride: 102.6 mmol/L; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Creatinine: 5.4 mg/dL; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Diastolic Blood Pressure: 112.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 18.0 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Glucose: 107.8 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Heart rate: 94.0 /min; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.6 %; type=numeric | **DIABETES** | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 49.6 mg/dL; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 141.3 mg/dL; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 219.7 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Potassium: 4.9 mmol/L; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Sodium: 142.6 mmol/L; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Systolic Blood Pressure: 170.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Total Cholesterol: 221.5 mg/dL; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Triglycerides: 153.4 mg/dL; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Lab Results | Urea Nitrogen: 12.0 mg/dL; type=numeric |  | observations.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=968.00 | **DIABETES** | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=147.12 | **HYPERTENSION** | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=138.48 |  | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=114.00 |  | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=1735.22 | **DIABETES** | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=266.18 |  | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=51.40 |  | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=144.10 |  | medications.csv |
| 2012-07-13 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=481.88 |  | medications.csv |
| 2012-08-10 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-08-10T21:06:21Z |  | encounters.csv |
| 2012-09-07 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-09-07T21:06:21Z |  | encounters.csv |
| 2012-09-14 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2012-09-14T21:21:21Z |  | encounters.csv |
| 2012-09-14 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Body Mass Index: 44.2 kg/m2; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Body Weight: 118.5 kg; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Calcium: 9.3 mg/dL; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Carbon Dioxide: 26.0 mmol/L; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Chloride: 107.9 mmol/L; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Creatinine: 4.2 mg/dL; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Diastolic Blood Pressure: 109.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.0 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Glucose: 117.7 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Heart rate: 69.0 /min; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.5 %; type=numeric | **DIABETES** | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 52.4 mg/dL; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 112.3 mg/dL; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 177.0 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Potassium: 5.0 mmol/L; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Sodium: 138.9 mmol/L; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Systolic Blood Pressure: 161.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Total Cholesterol: 203.9 mg/dL; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Triglycerides: 196.2 mg/dL; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Lab Results | Urea Nitrogen: 13.4 mg/dL; type=numeric |  | observations.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1582.59 | **DIABETES** | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=3; total cost=132.99 | **HYPERTENSION** | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=3; total cost=103.65 |  | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=325.14 |  | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=2309.40 | **DIABETES** | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=3; total cost=339.69 |  | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=3; total cost=22.35 |  | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=162.21 |  | medications.csv |
| 2012-09-14 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=89.55 |  | medications.csv |
| 2012-10-12 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-10-12T21:06:21Z |  | encounters.csv |
| 2012-12-07 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-12-07T21:06:21Z |  | encounters.csv |
| 2012-12-14 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2012-12-14T21:06:21Z |  | encounters.csv |
| 2013-01-04 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2013-01-04T21:21:21Z |  | encounters.csv |
| 2013-01-04 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Body Mass Index: 44.5 kg/m2; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Body Weight: 119.4 kg; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Carbon Dioxide: 25.2 mmol/L; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Chloride: 104.6 mmol/L; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Creatinine: 6.3 mg/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Diastolic Blood Pressure: 95.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Erythrocyte distribution width [Entitic volume] by Automated count: 43.7 fL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Erythrocytes [#/volume] in Blood by Automated count: 5.1 10*6/uL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 15.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Glucose: 109.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Heart rate: 67.0 /min; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Hematocrit [Volume Fraction] of Blood by Automated count: 35.7 %; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Hemoglobin [Mass/volume] in Blood: 15.5 g/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.6 %; type=numeric | **DIABETES** | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 55.0 mg/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Leukocytes [#/volume] in Blood by Automated count: 5.4 10*3/uL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 124.2 mg/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | MCH [Entitic mass] by Automated count: 31.8 pg; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | MCHC [Mass/volume] by Automated count: 34.4 g/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | MCV [Entitic volume] by Automated count: 90.1 fL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 138.5 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Platelet distribution width [Entitic volume] in Blood by Automated count: 459.5 fL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Platelet mean volume [Entitic volume] in Blood by Automated count: 10.1 fL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Platelets [#/volume] in Blood by Automated count: 170.9 10*3/uL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Potassium: 3.9 mmol/L; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Sodium: 139.1 mmol/L; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Systolic Blood Pressure: 192.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Total Cholesterol: 215.5 mg/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Triglycerides: 181.4 mg/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Lab Results | Urea Nitrogen: 12.4 mg/dL; type=numeric |  | observations.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=225.10 | **DIABETES** | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=30.89 | **HYPERTENSION** | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=58.51 |  | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=134.78 |  | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=618.58 | **DIABETES** | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=83.75 |  | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=24.59 |  | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=127.33 |  | medications.csv |
| 2013-01-04 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=31.76 |  | medications.csv |
| 2013-02-08 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2013-02-08T21:36:21Z |  | encounters.csv |
| 2013-02-08 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Body Mass Index: 44.6 kg/m2; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Body Weight: 119.7 kg; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Calcium: 8.8 mg/dL; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Carbon Dioxide: 22.9 mmol/L; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Chloride: 110.3 mmol/L; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Creatinine: 4.1 mg/dL; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Diastolic Blood Pressure: 103.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 24.1 mL/min/{1.73_m2}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Glucose: 101.9 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Heart rate: 94.0 /min; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.7 %; type=numeric | **DIABETES** | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 56.6 mg/dL; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 126.9 mg/dL; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 261.5 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Potassium: 4.5 mmol/L; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Sodium: 140.6 mmol/L; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Systolic Blood Pressure: 150.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Total Cholesterol: 216.0 mg/dL; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Triglycerides: 162.6 mg/dL; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Lab Results | Urea Nitrogen: 8.5 mg/dL; type=numeric |  | observations.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=96.92 | **DIABETES** | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=31.00 | **HYPERTENSION** | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=63.43 |  | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=73.32 |  | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=539.81 | **DIABETES** | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=236.67 |  | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=33.39 |  | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=128.58 |  | medications.csv |
| 2013-02-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=52.29 |  | medications.csv |
| 2013-02-14 20:51:21 | Lab Results | DALY: 27.7 a; type=numeric |  | observations.csv |
| 2013-02-14 20:51:21 | Lab Results | QALY: 43.3 a; type=numeric |  | observations.csv |
| 2013-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2013-02-15 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-02-15T21:06:21Z |  | encounters.csv |
| 2013-03-08 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-03-08T21:06:21Z |  | encounters.csv |
| 2013-03-15 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2013-03-15T21:21:21Z |  | encounters.csv |
| 2013-03-15 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Body Mass Index: 44.7 kg/m2; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Body Weight: 120.0 kg; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Carbon Dioxide: 21.2 mmol/L; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Chloride: 109.9 mmol/L; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Creatinine: 4.3 mg/dL; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Diastolic Blood Pressure: 109.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 22.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Glucose: 101.8 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Heart rate: 81.0 /min; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.7 %; type=numeric | **DIABETES** | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 53.2 mg/dL; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 133.5 mg/dL; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 61.6 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Sodium: 144.0 mmol/L; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Systolic Blood Pressure: 188.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Total Cholesterol: 225.4 mg/dL; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Triglycerides: 193.4 mg/dL; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Lab Results | Urea Nitrogen: 9.9 mg/dL; type=numeric |  | observations.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=112.40 | **DIABETES** | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=37.71 | **HYPERTENSION** | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=53.10 |  | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=110.39 |  | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1081.56 | **DIABETES** | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=81.42 |  | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=22.18 |  | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=107.83 |  | medications.csv |
| 2013-03-15 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=20.29 |  | medications.csv |
| 2013-04-05 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-04-05T21:06:21Z |  | encounters.csv |
| 2013-05-10 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2013-05-10T21:21:21Z |  | encounters.csv |
| 2013-05-10 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Body Mass Index: 44.9 kg/m2; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Body Weight: 120.5 kg; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Calcium: 8.9 mg/dL; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Carbon Dioxide: 23.4 mmol/L; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Chloride: 105.3 mmol/L; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Creatinine: 6.2 mg/dL; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Diastolic Blood Pressure: 97.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 15.5 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Glucose: 116.6 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Heart rate: 91.0 /min; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.7 %; type=numeric | **DIABETES** | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 56.3 mg/dL; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 113.4 mg/dL; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 104.4 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Potassium: 4.3 mmol/L; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Sodium: 142.3 mmol/L; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Systolic Blood Pressure: 183.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Total Cholesterol: 203.9 mg/dL; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Triglycerides: 171.3 mg/dL; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Lab Results | Urea Nitrogen: 12.8 mg/dL; type=numeric |  | observations.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=330.44 | **DIABETES** | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=4.76 | **HYPERTENSION** | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=88.51 |  | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=17.78 |  | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=791.41 | **DIABETES** | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=108.94 |  | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=23.11 |  | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=194.05 |  | medications.csv |
| 2013-05-10 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=72.12 |  | medications.csv |
| 2013-06-07 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-06-07T21:06:21Z |  | encounters.csv |
| 2013-07-05 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2013-07-05T21:21:21Z |  | encounters.csv |
| 2013-07-05 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Body Mass Index: 45.1 kg/m2; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Body Weight: 120.9 kg; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Calcium: 8.7 mg/dL; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Carbon Dioxide: 21.0 mmol/L; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Chloride: 108.1 mmol/L; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Creatinine: 3.6 mg/dL; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Diastolic Blood Pressure: 103.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 27.1 mL/min/{1.73_m2}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Glucose: 113.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Heart rate: 95.0 /min; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.8 %; type=numeric | **DIABETES** | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 56.5 mg/dL; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 143.9 mg/dL; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 93.5 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Potassium: 4.1 mmol/L; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Sodium: 137.0 mmol/L; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Systolic Blood Pressure: 170.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Total Cholesterol: 231.1 mg/dL; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Triglycerides: 153.7 mg/dL; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Lab Results | Urea Nitrogen: 7.6 mg/dL; type=numeric |  | observations.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=537.38 | **DIABETES** | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=27.48 | **HYPERTENSION** | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=56.58 |  | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=50.61 |  | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=484.74 | **DIABETES** | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=116.23 |  | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=33.33 |  | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=85.65 |  | medications.csv |
| 2013-07-05 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=26.56 |  | medications.csv |
| 2013-08-02 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2013-08-02T21:21:21Z |  | encounters.csv |
| 2013-08-02 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Body Mass Index: 45.2 kg/m2; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Body Weight: 121.2 kg; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Calcium: 9.1 mg/dL; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Carbon Dioxide: 20.1 mmol/L; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Chloride: 105.6 mmol/L; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Creatinine: 4.2 mg/dL; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Diastolic Blood Pressure: 91.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.0 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Glucose: 110.3 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Heart rate: 98.0 /min; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.8 %; type=numeric | **DIABETES** | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 49.2 mg/dL; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 141.4 mg/dL; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 81.5 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Potassium: 4.4 mmol/L; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Sodium: 136.6 mmol/L; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Systolic Blood Pressure: 181.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Total Cholesterol: 221.5 mg/dL; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Triglycerides: 154.3 mg/dL; type=numeric |  | observations.csv |
| 2013-08-02 20:51:21 | Lab Results | Urea Nitrogen: 14.0 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=778.16 | **DIABETES** | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=4; total cost=210.20 | **HYPERTENSION** | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=4; total cost=488.60 |  | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=122.28 |  | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=4202.24 | **DIABETES** | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=4; total cost=788.48 |  | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=4; total cost=101.92 |  | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=786.16 |  | medications.csv |
| 2013-08-02 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=251.52 |  | medications.csv |
| 2013-09-06 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-09-06T21:06:21Z |  | encounters.csv |
| 2013-09-13 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-09-13T21:06:21Z |  | encounters.csv |
| 2013-10-04 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-10-04T21:06:21Z |  | encounters.csv |
| 2013-10-11 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-10-11T21:06:21Z |  | encounters.csv |
| 2013-11-01 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-11-01T21:06:21Z |  | encounters.csv |
| 2013-12-06 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2013-12-06T21:06:21Z |  | encounters.csv |
| 2013-12-13 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2013-12-13T21:21:21Z |  | encounters.csv |
| 2013-12-13 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Body Mass Index: 45.6 kg/m2; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Body Weight: 122.3 kg; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Calcium: 8.8 mg/dL; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Carbon Dioxide: 21.3 mmol/L; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Chloride: 105.7 mmol/L; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Creatinine: 4.4 mg/dL; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Diastolic Blood Pressure: 110.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 22.1 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Glucose: 124.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Heart rate: 79.0 /min; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.9 %; type=numeric | **DIABETES** | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 44.9 mg/dL; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 123.8 mg/dL; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 95.6 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Potassium: 5.0 mmol/L; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Sodium: 136.9 mmol/L; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Systolic Blood Pressure: 180.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Total Cholesterol: 201.1 mg/dL; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Triglycerides: 162.0 mg/dL; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Lab Results | Urea Nitrogen: 15.3 mg/dL; type=numeric |  | observations.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=583.82 | **DIABETES** | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=120.70 | **HYPERTENSION** | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=194.94 |  | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=197.08 |  | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=3608.08 | **DIABETES** | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=119.52 |  | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=9.48 |  | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=458.02 |  | medications.csv |
| 2013-12-13 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=148.62 |  | medications.csv |
| 2014-01-03 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-01-03T21:06:21Z |  | encounters.csv |
| 2014-02-14 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2014-02-14T21:21:21Z |  | encounters.csv |
| 2014-02-14 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Body Mass Index: 45.8 kg/m2; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Body Weight: 122.8 kg; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Calcium: 9.3 mg/dL; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Carbon Dioxide: 25.6 mmol/L; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Chloride: 102.5 mmol/L; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Creatinine: 3.7 mg/dL; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | DALY: 28.2 a; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Diastolic Blood Pressure: 112.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 26.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Glucose: 106.2 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Heart rate: 75.0 /min; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 3.9 %; type=numeric | **DIABETES** | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 45.9 mg/dL; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 144.0 mg/dL; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 194.3 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Potassium: 4.9 mmol/L; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | QALY: 43.8 a; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Sodium: 142.9 mmol/L; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Systolic Blood Pressure: 145.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Total Cholesterol: 226.9 mg/dL; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Triglycerides: 185.1 mg/dL; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Lab Results | Urea Nitrogen: 16.8 mg/dL; type=numeric |  | observations.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=274.11 | **DIABETES** | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=42.18 | **HYPERTENSION** | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=50.06 |  | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=100.47 |  | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=995.69 | **DIABETES** | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=20.05 |  | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=22.30 |  | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=148.58 |  | medications.csv |
| 2014-02-14 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=68.94 |  | medications.csv |
| 2014-02-21 00:00:00 | Diagnoses | Otitis media code=65363002; recorded stop=2014-04-11 |  | conditions.csv |
| 2014-02-21 20:51:21 | Encounters | Encounter for symptom; class=outpatient; reason=Otitis media; end=2014-02-21T21:06:21Z |  | encounters.csv |
| 2014-02-21 20:51:21 | Medications Started | Acetaminophen 325 MG Oral Tablet code=313782; dispenses=1; total cost=5.91 |  | medications.csv |
| 2014-02-28 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2014-02-28T21:21:21Z |  | encounters.csv |
| 2014-02-28 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Body Mass Index: 45.8 kg/m2; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Body Weight: 122.9 kg; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Carbon Dioxide: 24.7 mmol/L; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Chloride: 107.7 mmol/L; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Creatinine: 3.6 mg/dL; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Diastolic Blood Pressure: 95.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 27.1 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Glucose: 116.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Heart rate: 89.0 /min; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.0 %; type=numeric | **DIABETES** | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 53.2 mg/dL; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 114.0 mg/dL; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 245.9 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Potassium: 4.0 mmol/L; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Sodium: 136.8 mmol/L; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Systolic Blood Pressure: 166.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Total Cholesterol: 200.1 mg/dL; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Triglycerides: 164.6 mg/dL; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Lab Results | Urea Nitrogen: 11.4 mg/dL; type=numeric |  | observations.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=393.01 | **DIABETES** | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=37.14 | **HYPERTENSION** | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=95.21 |  | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=125.34 |  | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=196.17 | **DIABETES** | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=321.83 |  | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=38.42 |  | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=167.81 |  | medications.csv |
| 2014-02-28 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=50.20 |  | medications.csv |
| 2014-03-07 20:51:21 | Medication Changes | Stopped/ended: Acetaminophen 325 MG Oral Tablet code=313782 | **MEDICATION CHANGE** | medications.csv |
| 2014-04-04 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-04-04T21:06:21Z |  | encounters.csv |
| 2014-04-11 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2014-04-11T21:21:21Z |  | encounters.csv |
| 2014-04-11 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Body Mass Index: 45.9 kg/m2; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Body Weight: 123.3 kg; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Calcium: 8.5 mg/dL; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Carbon Dioxide: 21.6 mmol/L; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Chloride: 106.7 mmol/L; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Creatinine: 6.0 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Diastolic Blood Pressure: 102.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.2 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Glucose: 117.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Heart rate: 62.0 /min; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.0 %; type=numeric | **DIABETES** | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 50.2 mg/dL; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 127.9 mg/dL; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 225.3 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Potassium: 4.4 mmol/L; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Sodium: 136.1 mmol/L; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Systolic Blood Pressure: 171.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Total Cholesterol: 214.3 mg/dL; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Triglycerides: 180.9 mg/dL; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Lab Results | Urea Nitrogen: 11.8 mg/dL; type=numeric |  | observations.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=5.87 | **DIABETES** | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=23.19 | **HYPERTENSION** | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=34.99 |  | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=76.51 |  | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1337.01 | **DIABETES** | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=136.25 |  | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=33.84 |  | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=43.00 |  | medications.csv |
| 2014-04-11 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=73.28 |  | medications.csv |
| 2014-05-02 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2014-05-02T21:21:21Z |  | encounters.csv |
| 2014-05-02 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Body Mass Index: 46.0 kg/m2; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Body Weight: 123.4 kg; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Calcium: 8.9 mg/dL; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Carbon Dioxide: 26.4 mmol/L; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Chloride: 110.2 mmol/L; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Creatinine: 3.8 mg/dL; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Diastolic Blood Pressure: 97.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 25.7 mL/min/{1.73_m2}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Glucose: 107.2 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Heart rate: 90.0 /min; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.0 %; type=numeric | **DIABETES** | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 52.2 mg/dL; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 120.5 mg/dL; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 139.9 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Potassium: 3.8 mmol/L; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Sodium: 137.0 mmol/L; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Systolic Blood Pressure: 171.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Total Cholesterol: 208.8 mg/dL; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Triglycerides: 180.2 mg/dL; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Lab Results | Urea Nitrogen: 17.0 mg/dL; type=numeric |  | observations.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=265.69 | **DIABETES** | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=72.13 | **HYPERTENSION** | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=102.79 |  | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=101.77 |  | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=114.59 | **DIABETES** | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=55.60 |  | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=14.33 |  | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=37.33 |  | medications.csv |
| 2014-05-02 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=85.97 |  | medications.csv |
| 2014-05-30 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-05-30T21:06:21Z |  | encounters.csv |
| 2014-06-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2014-06-06T21:21:21Z |  | encounters.csv |
| 2014-06-06 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Body Mass Index: 46.1 kg/m2; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Body Weight: 123.7 kg; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Calcium: 9.2 mg/dL; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Carbon Dioxide: 21.1 mmol/L; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Chloride: 101.3 mmol/L; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Creatinine: 5.9 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Diastolic Blood Pressure: 98.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Glucose: 109.9 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Heart rate: 70.0 /min; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.0 %; type=numeric | **DIABETES** | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 56.3 mg/dL; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 148.2 mg/dL; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 159.7 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Potassium: 4.1 mmol/L; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Sodium: 142.6 mmol/L; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Systolic Blood Pressure: 194.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Total Cholesterol: 235.1 mg/dL; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Triglycerides: 152.8 mg/dL; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Lab Results | Urea Nitrogen: 19.4 mg/dL; type=numeric |  | observations.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=302.14 | **DIABETES** | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=16.63 | **HYPERTENSION** | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=10.19 |  | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=76.90 |  | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=850.37 | **DIABETES** | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=214.27 |  | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=10.86 |  | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=77.62 |  | medications.csv |
| 2014-06-06 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=64.91 |  | medications.csv |
| 2014-07-04 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-07-04T21:06:21Z |  | encounters.csv |
| 2014-07-11 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2014-07-11T21:21:21Z |  | encounters.csv |
| 2014-07-11 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Body Mass Index: 46.2 kg/m2; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Body Weight: 124.0 kg; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Calcium: 9.6 mg/dL; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Carbon Dioxide: 20.6 mmol/L; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Chloride: 109.2 mmol/L; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Creatinine: 5.4 mg/dL; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Diastolic Blood Pressure: 108.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 18.3 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Glucose: 115.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Heart rate: 80.0 /min; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.1 %; type=numeric | **DIABETES** | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 42.2 mg/dL; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 128.1 mg/dL; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 83.7 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Potassium: 4.3 mmol/L; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Sodium: 136.8 mmol/L; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Systolic Blood Pressure: 189.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Total Cholesterol: 202.6 mg/dL; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Triglycerides: 161.4 mg/dL; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Lab Results | Urea Nitrogen: 11.3 mg/dL; type=numeric |  | observations.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=51.88 | **DIABETES** | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=57.66 | **HYPERTENSION** | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=201.74 |  | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=239.92 |  | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=645.20 | **DIABETES** | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=85.50 |  | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=24.24 |  | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=156.80 |  | medications.csv |
| 2014-07-11 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=185.04 |  | medications.csv |
| 2014-08-01 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-08-01T21:06:21Z |  | encounters.csv |
| 2014-09-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2014-09-26T21:21:21Z |  | encounters.csv |
| 2014-09-26 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Body Mass Index: 46.5 kg/m2; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Body Weight: 124.7 kg; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Calcium: 8.8 mg/dL; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Carbon Dioxide: 22.7 mmol/L; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Chloride: 103.3 mmol/L; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Creatinine: 4.2 mg/dL; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Diastolic Blood Pressure: 108.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Glucose: 103.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Heart rate: 63.0 /min; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.1 %; type=numeric | **DIABETES** | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 58.4 mg/dL; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 138.6 mg/dL; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 41.4 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Potassium: 3.8 mmol/L; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Sodium: 139.1 mmol/L; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Systolic Blood Pressure: 151.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Total Cholesterol: 233.7 mg/dL; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Triglycerides: 183.7 mg/dL; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Lab Results | Urea Nitrogen: 12.7 mg/dL; type=numeric |  | observations.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=108.65 | **DIABETES** | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=15.68 | **HYPERTENSION** | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=28.53 |  | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=47.10 |  | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=115.27 | **DIABETES** | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=84.92 |  | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=14.94 |  | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=138.96 |  | medications.csv |
| 2014-09-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=99.90 |  | medications.csv |
| 2014-10-31 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-10-31T21:06:21Z |  | encounters.csv |
| 2014-11-07 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2014-11-07T21:21:21Z |  | encounters.csv |
| 2014-11-07 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Body Mass Index: 46.6 kg/m2; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Body Weight: 125.0 kg; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Carbon Dioxide: 23.8 mmol/L; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Chloride: 108.7 mmol/L; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Creatinine: 4.3 mg/dL; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Diastolic Blood Pressure: 105.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.2 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Glucose: 113.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Heart rate: 75.0 /min; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.2 %; type=numeric | **DIABETES** | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 51.9 mg/dL; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 119.4 mg/dL; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 223.0 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Potassium: 4.9 mmol/L; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Sodium: 143.8 mmol/L; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Systolic Blood Pressure: 160.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Total Cholesterol: 207.4 mg/dL; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Triglycerides: 180.2 mg/dL; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Lab Results | Urea Nitrogen: 10.6 mg/dL; type=numeric |  | observations.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=234.88 | **DIABETES** | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=50.90 | **HYPERTENSION** | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=90.26 |  | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=27.16 |  | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=139.21 | **DIABETES** | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=56.68 |  | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=22.04 |  | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=54.81 |  | medications.csv |
| 2014-11-07 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=31.14 |  | medications.csv |
| 2014-11-28 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-11-28T21:06:21Z |  | encounters.csv |
| 2014-12-26 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2014-12-26T21:06:21Z |  | encounters.csv |
| 2015-01-02 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2015-01-02T21:21:21Z |  | encounters.csv |
| 2015-01-02 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Body Mass Index: 46.8 kg/m2; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Body Weight: 125.5 kg; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Calcium: 10.2 mg/dL; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Carbon Dioxide: 22.3 mmol/L; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Chloride: 108.2 mmol/L; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Creatinine: 6.4 mg/dL; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Diastolic Blood Pressure: 108.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 15.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Glucose: 116.9 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Heart rate: 88.0 /min; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.2 %; type=numeric | **DIABETES** | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 55.4 mg/dL; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 146.9 mg/dL; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 39.6 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Potassium: 4.7 mmol/L; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Sodium: 138.1 mmol/L; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Systolic Blood Pressure: 154.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Total Cholesterol: 234.4 mg/dL; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Triglycerides: 160.5 mg/dL; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Lab Results | Urea Nitrogen: 12.6 mg/dL; type=numeric |  | observations.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=11.62 | **DIABETES** | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=57.53 | **HYPERTENSION** | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=23.00 |  | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=48.34 |  | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=792.96 | **DIABETES** | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=196.83 |  | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=6.39 |  | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=171.93 |  | medications.csv |
| 2015-01-02 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=147.34 |  | medications.csv |
| 2015-01-30 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-01-30T21:06:21Z |  | encounters.csv |
| 2015-02-14 20:51:21 | Lab Results | DALY: 28.8 a; type=numeric |  | observations.csv |
| 2015-02-14 20:51:21 | Lab Results | QALY: 44.2 a; type=numeric |  | observations.csv |
| 2015-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2015-02-20T21:36:21Z |  | encounters.csv |
| 2015-02-20 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Body Mass Index: 46.9 kg/m2; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Body Weight: 125.9 kg; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Calcium: 10.1 mg/dL; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Carbon Dioxide: 27.8 mmol/L; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Chloride: 110.9 mmol/L; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Creatinine: 4.4 mg/dL; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Diastolic Blood Pressure: 101.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 22.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Glucose: 110.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Heart rate: 75.0 /min; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.2 %; type=numeric | **DIABETES** | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 41.6 mg/dL; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 156.7 mg/dL; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 99.2 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Potassium: 4.1 mmol/L; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Sodium: 142.2 mmol/L; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Systolic Blood Pressure: 152.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Total Cholesterol: 236.3 mg/dL; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Triglycerides: 189.9 mg/dL; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Lab Results | Urea Nitrogen: 18.8 mg/dL; type=numeric |  | observations.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=719.40 | **DIABETES** | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=3; total cost=43.17 | **HYPERTENSION** | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=3; total cost=324.93 |  | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=266.58 |  | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=1401.03 | **DIABETES** | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=3; total cost=60.21 |  | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=3; total cost=54.99 |  | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=111.00 |  | medications.csv |
| 2015-02-20 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=313.20 |  | medications.csv |
| 2015-03-27 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-03-27T21:06:21Z |  | encounters.csv |
| 2015-04-24 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-04-24T21:06:21Z |  | encounters.csv |
| 2015-05-29 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-05-29T21:06:21Z |  | encounters.csv |
| 2015-06-06 00:00:00 | Diagnoses | Viral sinusitis (disorder) code=444814009; recorded stop=2015-06-27 |  | conditions.csv |
| 2015-06-05 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2015-06-05T21:21:21Z |  | encounters.csv |
| 2015-06-05 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Body Mass Index: 47.3 kg/m2; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Body Weight: 126.8 kg; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Carbon Dioxide: 27.4 mmol/L; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Chloride: 102.4 mmol/L; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Creatinine: 6.2 mg/dL; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Diastolic Blood Pressure: 100.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.0 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Glucose: 117.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Heart rate: 74.0 /min; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.3 %; type=numeric | **DIABETES** | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 49.0 mg/dL; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 154.6 mg/dL; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 200.4 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Potassium: 3.9 mmol/L; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Sodium: 140.1 mmol/L; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Systolic Blood Pressure: 171.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Total Cholesterol: 235.5 mg/dL; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Triglycerides: 159.3 mg/dL; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Lab Results | Urea Nitrogen: 16.6 mg/dL; type=numeric |  | observations.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=194.66 | **DIABETES** | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=32.61 | **HYPERTENSION** | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=96.21 |  | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=94.59 |  | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=307.56 | **DIABETES** | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=128.02 |  | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=3.44 |  | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=32.98 |  | medications.csv |
| 2015-06-05 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=16.62 |  | medications.csv |
| 2015-06-06 20:51:21 | Encounters | Encounter for symptom; class=ambulatory; reason=Viral sinusitis (disorder); end=2015-06-06T21:06:21Z |  | encounters.csv |
| 2015-06-12 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-06-12T21:06:21Z |  | encounters.csv |
| 2015-06-19 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-06-19T21:06:21Z |  | encounters.csv |
| 2015-06-26 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-06-26T21:06:21Z |  | encounters.csv |
| 2015-07-03 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-07-03T21:06:21Z |  | encounters.csv |
| 2015-07-24 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-07-24T21:06:21Z |  | encounters.csv |
| 2015-07-31 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2015-07-31T21:21:21Z |  | encounters.csv |
| 2015-07-31 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Body Mass Index: 47.4 kg/m2; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Body Weight: 127.2 kg; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Carbon Dioxide: 28.2 mmol/L; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Chloride: 104.4 mmol/L; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Creatinine: 4.4 mg/dL; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Diastolic Blood Pressure: 102.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 22.5 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Glucose: 115.3 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Heart rate: 82.0 /min; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.4 %; type=numeric | **DIABETES** | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 52.5 mg/dL; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 129.5 mg/dL; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 92.8 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Potassium: 4.3 mmol/L; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Sodium: 140.0 mmol/L; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Systolic Blood Pressure: 161.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Total Cholesterol: 221.6 mg/dL; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Triglycerides: 198.4 mg/dL; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Lab Results | Urea Nitrogen: 9.3 mg/dL; type=numeric |  | observations.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=168.43 | **DIABETES** | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=22.20 | **HYPERTENSION** | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=90.15 |  | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=28.51 |  | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=982.13 | **DIABETES** | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=263.19 |  | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=25.83 |  | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=150.73 |  | medications.csv |
| 2015-07-31 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=94.29 |  | medications.csv |
| 2015-08-28 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2015-08-28T21:21:21Z |  | encounters.csv |
| 2015-08-28 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Body Mass Index: 47.5 kg/m2; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Body Weight: 127.5 kg; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Calcium: 9.1 mg/dL; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Carbon Dioxide: 25.1 mmol/L; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Chloride: 103.7 mmol/L; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Creatinine: 3.5 mg/dL; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Diastolic Blood Pressure: 100.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 28.5 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Glucose: 115.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Heart rate: 78.0 /min; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.4 %; type=numeric | **DIABETES** | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 41.2 mg/dL; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 140.6 mg/dL; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 174.3 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Sodium: 140.9 mmol/L; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Systolic Blood Pressure: 148.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Total Cholesterol: 219.6 mg/dL; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Triglycerides: 188.9 mg/dL; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Lab Results | Urea Nitrogen: 8.4 mg/dL; type=numeric |  | observations.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=499.40 | **DIABETES** | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=22.28 | **HYPERTENSION** | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=51.83 |  | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=64.49 |  | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=523.42 | **DIABETES** | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=316.18 |  | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=38.79 |  | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=60.36 |  | medications.csv |
| 2015-08-28 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=189.65 |  | medications.csv |
| 2015-09-25 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-09-25T21:06:21Z |  | encounters.csv |
| 2015-10-23 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2015-10-23T21:21:21Z |  | encounters.csv |
| 2015-10-23 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Body Mass Index: 47.7 kg/m2; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Body Weight: 127.9 kg; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Calcium: 10.0 mg/dL; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Carbon Dioxide: 25.4 mmol/L; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Chloride: 103.1 mmol/L; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Creatinine: 5.7 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Diastolic Blood Pressure: 105.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 17.5 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Glucose: 113.3 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Heart rate: 65.0 /min; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.4 %; type=numeric | **DIABETES** | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 58.3 mg/dL; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 112.6 mg/dL; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 158.4 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Potassium: 3.9 mmol/L; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Sodium: 137.1 mmol/L; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Systolic Blood Pressure: 184.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Total Cholesterol: 207.3 mg/dL; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Triglycerides: 181.7 mg/dL; type=numeric |  | observations.csv |
| 2015-10-23 20:51:21 | Lab Results | Urea Nitrogen: 18.9 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=54.60 | **DIABETES** | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=36.17 | **HYPERTENSION** | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=29.16 |  | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=42.88 |  | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=449.13 | **DIABETES** | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=31.97 |  | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=37.19 |  | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=59.76 |  | medications.csv |
| 2015-10-23 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=95.11 |  | medications.csv |
| 2015-11-20 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-11-20T21:06:21Z |  | encounters.csv |
| 2015-11-27 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2015-11-27T21:21:21Z |  | encounters.csv |
| 2015-11-27 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Body Mass Index: 47.8 kg/m2; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Body Weight: 128.2 kg; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Carbon Dioxide: 25.1 mmol/L; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Chloride: 110.2 mmol/L; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Creatinine: 4.0 mg/dL; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Diastolic Blood Pressure: 112.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 25.2 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Glucose: 122.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Heart rate: 81.0 /min; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.4 %; type=numeric | **DIABETES** | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 54.2 mg/dL; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 138.2 mg/dL; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 71.2 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Potassium: 4.4 mmol/L; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Sodium: 136.2 mmol/L; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Systolic Blood Pressure: 152.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Total Cholesterol: 227.8 mg/dL; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Triglycerides: 177.1 mg/dL; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Lab Results | Urea Nitrogen: 19.8 mg/dL; type=numeric |  | observations.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=3; total cost=1675.23 | **DIABETES** | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=3; total cost=790.47 | **HYPERTENSION** | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=3; total cost=111.51 | **HYPERTENSION** | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=3; total cost=138.30 |  | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=3; total cost=303.48 |  | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=3; total cost=2888.52 | **DIABETES** | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=3; total cost=796.98 |  | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=3; total cost=58.98 |  | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=3; total cost=627.78 |  | medications.csv |
| 2015-11-27 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=3; total cost=184.56 |  | medications.csv |
| 2015-12-25 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2015-12-25T21:06:21Z |  | encounters.csv |
| 2016-02-14 20:51:21 | Lab Results | DALY: 29.3 a; type=numeric |  | observations.csv |
| 2016-02-14 20:51:21 | Lab Results | QALY: 44.7 a; type=numeric |  | observations.csv |
| 2016-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2016-02-19 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-02-19T21:06:21Z |  | encounters.csv |
| 2016-02-26 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2016-02-26T21:21:21Z |  | encounters.csv |
| 2016-02-26 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Body Mass Index: 48.1 kg/m2; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Body Weight: 129.0 kg; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Calcium: 8.8 mg/dL; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Carbon Dioxide: 20.8 mmol/L; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Chloride: 104.0 mmol/L; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Creatinine: 4.2 mg/dL; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Diastolic Blood Pressure: 111.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Glucose: 116.8 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Heart rate: 82.0 /min; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 51.4 mg/dL; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 147.4 mg/dL; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 141.1 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Sodium: 138.0 mmol/L; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Systolic Blood Pressure: 190.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Total Cholesterol: 235.5 mg/dL; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Triglycerides: 183.3 mg/dL; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Lab Results | Urea Nitrogen: 13.2 mg/dL; type=numeric |  | observations.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=1186.36 | **DIABETES** | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=4; total cost=251.44 | **HYPERTENSION** | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=4; total cost=103.80 |  | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=551.32 |  | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=2913.52 | **DIABETES** | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=4; total cost=840.40 |  | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=4; total cost=77.28 |  | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=144.04 |  | medications.csv |
| 2016-02-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=313.16 |  | medications.csv |
| 2016-03-25 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-03-25T21:06:21Z |  | encounters.csv |
| 2016-04-22 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-04-22T21:06:21Z |  | encounters.csv |
| 2016-07-22 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2016-07-22T21:21:21Z |  | encounters.csv |
| 2016-07-22 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Calcium: 9.8 mg/dL; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Carbon Dioxide: 21.7 mmol/L; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Chloride: 103.2 mmol/L; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Creatinine: 4.5 mg/dL; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Diastolic Blood Pressure: 114.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 22.5 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Glucose: 116.8 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Heart rate: 61.0 /min; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 40.2 mg/dL; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 148.5 mg/dL; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 59.9 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Potassium: 3.8 mmol/L; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Sodium: 140.6 mmol/L; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Systolic Blood Pressure: 164.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Total Cholesterol: 220.3 mg/dL; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Triglycerides: 158.3 mg/dL; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Lab Results | Urea Nitrogen: 17.9 mg/dL; type=numeric |  | observations.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=159.51 | **DIABETES** | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=24.17 | **HYPERTENSION** | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=6.25 |  | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=63.85 |  | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1067.66 | **DIABETES** | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=187.57 |  | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=32.90 |  | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=132.14 |  | medications.csv |
| 2016-07-22 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=232.90 |  | medications.csv |
| 2016-08-19 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-08-19T21:06:21Z |  | encounters.csv |
| 2016-08-26 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-08-26T21:06:21Z |  | encounters.csv |
| 2016-09-16 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2016-09-16T21:21:21Z |  | encounters.csv |
| 2016-09-16 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Calcium: 8.5 mg/dL; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Carbon Dioxide: 23.4 mmol/L; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Chloride: 105.1 mmol/L; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Creatinine: 5.7 mg/dL; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Diastolic Blood Pressure: 110.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 17.5 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Glucose: 117.2 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Heart rate: 74.0 /min; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 42.3 mg/dL; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 162.8 mg/dL; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 61.5 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Potassium: 3.7 mmol/L; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Sodium: 140.1 mmol/L; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Systolic Blood Pressure: 190.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Total Cholesterol: 239.0 mg/dL; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Triglycerides: 169.7 mg/dL; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Lab Results | Urea Nitrogen: 16.7 mg/dL; type=numeric |  | observations.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=507.14 | **DIABETES** | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=40.54 | **HYPERTENSION** | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=66.70 |  | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=62.66 |  | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=944.90 | **DIABETES** | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=141.04 |  | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=27.24 |  | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=88.92 |  | medications.csv |
| 2016-09-16 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=141.78 |  | medications.csv |
| 2016-10-13 00:00:00 | Diagnoses | Fracture of forearm code=65966004; recorded stop=2017-01-11 |  | conditions.csv |
| 2016-10-13 20:51:21 | Encounters | Emergency room admission (procedure); class=emergency; end=2016-10-13T23:14:21Z |  | encounters.csv |
| 2016-10-13 20:51:21 | Lab Results | DXA [T-score] Bone density: -0.0 {T-score}; type=numeric |  | observations.csv |
| 2016-10-13 20:51:21 | Medications Started | Acetaminophen 325 MG / HYDROcodone Bitartrate 7.5 MG Oral Tablet code=857005; dispenses=1; total cost=42.18 |  | medications.csv |
| 2016-10-13 20:51:21 | Medications Started | Acetaminophen 325 MG Oral Tablet code=313782; dispenses=3; total cost=17.22 |  | medications.csv |
| 2016-10-21 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-10-21T21:06:21Z |  | encounters.csv |
| 2016-11-18 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-11-18T21:06:21Z |  | encounters.csv |
| 2016-11-25 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2016-11-25T21:21:21Z |  | encounters.csv |
| 2016-11-25 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Calcium: 9.9 mg/dL; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Carbon Dioxide: 21.9 mmol/L; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Chloride: 103.3 mmol/L; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Creatinine: 5.7 mg/dL; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Diastolic Blood Pressure: 97.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 17.7 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Glucose: 120.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Heart rate: 86.0 /min; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 44.4 mg/dL; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 121.7 mg/dL; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 246.3 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Potassium: 4.6 mmol/L; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Sodium: 141.7 mmol/L; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Systolic Blood Pressure: 176.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Total Cholesterol: 205.1 mg/dL; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Triglycerides: 195.3 mg/dL; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Lab Results | Urea Nitrogen: 13.9 mg/dL; type=numeric |  | observations.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=237.13 | **DIABETES** | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=5.76 | **HYPERTENSION** | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=95.37 |  | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=89.24 |  | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=224.48 | **DIABETES** | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=81.79 |  | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=13.79 |  | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=243.15 |  | medications.csv |
| 2016-11-25 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=59.40 |  | medications.csv |
| 2016-11-26 20:51:21 | Medication Changes | Stopped/ended: Acetaminophen 325 MG / HYDROcodone Bitartrate 7.5 MG Oral Tablet code=857005 | **MEDICATION CHANGE** | medications.csv |
| 2016-12-16 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2016-12-16T21:06:21Z |  | encounters.csv |
| 2017-01-11 20:51:21 | Encounters | Encounter for 'check-up'; class=ambulatory; reason=Fracture of forearm; end=2017-01-11T21:06:21Z |  | encounters.csv |
| 2017-01-11 20:51:21 | Medication Changes | Stopped/ended: Acetaminophen 325 MG Oral Tablet code=313782 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-01-13T21:21:21Z |  | encounters.csv |
| 2017-01-13 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Calcium: 9.2 mg/dL; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Carbon Dioxide: 22.6 mmol/L; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Chloride: 106.4 mmol/L; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Creatinine: 3.5 mg/dL; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Diastolic Blood Pressure: 103.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 28.6 mL/min/{1.73_m2}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Glucose: 102.9 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Heart rate: 96.0 /min; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 51.4 mg/dL; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 137.6 mg/dL; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 175.8 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Potassium: 4.9 mmol/L; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Sodium: 138.8 mmol/L; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Systolic Blood Pressure: 182.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Total Cholesterol: 223.5 mg/dL; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Triglycerides: 172.3 mg/dL; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Lab Results | Urea Nitrogen: 19.0 mg/dL; type=numeric |  | observations.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=253.29 | **DIABETES** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=96.56 | **DIABETES** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=43.29 | **HYPERTENSION** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=84.14 | **HYPERTENSION** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=11.94 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=21.55 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=140.65 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=71.22 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1074.34 | **DIABETES** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=476.54 | **DIABETES** | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=232.70 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=99.17 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=22.88 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=44.56 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=127.14 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=217.22 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=30.70 |  | medications.csv |
| 2017-01-13 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=69.02 |  | medications.csv |
| 2017-02-14 20:51:21 | Lab Results | DALY: 29.8 a; type=numeric |  | observations.csv |
| 2017-02-14 20:51:21 | Lab Results | QALY: 45.2 a; type=numeric |  | observations.csv |
| 2017-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-02-17T21:21:21Z |  | encounters.csv |
| 2017-02-17 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Carbon Dioxide: 24.3 mmol/L; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Chloride: 107.8 mmol/L; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Creatinine: 4.1 mg/dL; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Diastolic Blood Pressure: 104.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 24.2 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Glucose: 109.1 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Heart rate: 90.0 /min; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 41.9 mg/dL; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 148.7 mg/dL; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 56.2 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Potassium: 5.2 mmol/L; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Sodium: 142.6 mmol/L; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Systolic Blood Pressure: 177.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Total Cholesterol: 223.0 mg/dL; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Triglycerides: 162.1 mg/dL; type=numeric |  | observations.csv |
| 2017-02-17 20:51:21 | Lab Results | Urea Nitrogen: 7.4 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=35.26 | **DIABETES** | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=49.35 | **HYPERTENSION** | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=118.13 |  | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=48.46 |  | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=826.57 | **DIABETES** | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=163.36 |  | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=11.94 |  | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=219.55 |  | medications.csv |
| 2017-02-17 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=20.40 |  | medications.csv |
| 2017-03-03 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2017-03-03T21:21:21Z |  | encounters.csv |
| 2017-03-03 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Calcium: 8.7 mg/dL; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Carbon Dioxide: 23.0 mmol/L; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Chloride: 106.5 mmol/L; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Creatinine: 5.7 mg/dL; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Diastolic Blood Pressure: 93.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 17.3 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Glucose: 121.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Heart rate: 83.0 /min; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 53.8 mg/dL; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 118.0 mg/dL; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 176.9 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Potassium: 4.2 mmol/L; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Sodium: 139.4 mmol/L; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Systolic Blood Pressure: 177.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Total Cholesterol: 205.4 mg/dL; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Triglycerides: 168.1 mg/dL; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Lab Results | Urea Nitrogen: 10.4 mg/dL; type=numeric |  | observations.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=169.20 | **DIABETES** | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=61.07 | **HYPERTENSION** | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=83.45 |  | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=70.98 |  | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=767.55 | **DIABETES** | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=202.06 |  | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=27.42 |  | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=173.87 |  | medications.csv |
| 2017-03-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=23.29 |  | medications.csv |
| 2017-03-17 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2017-03-17T21:06:21Z |  | encounters.csv |
| 2017-04-14 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-04-14T21:21:21Z |  | encounters.csv |
| 2017-04-14 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Calcium: 10.1 mg/dL; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Carbon Dioxide: 22.9 mmol/L; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Chloride: 101.9 mmol/L; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Creatinine: 5.8 mg/dL; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Diastolic Blood Pressure: 116.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.9 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Glucose: 114.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Heart rate: 63.0 /min; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 40.3 mg/dL; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 133.4 mg/dL; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 113.5 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Sodium: 143.0 mmol/L; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Systolic Blood Pressure: 176.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Total Cholesterol: 208.5 mg/dL; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Triglycerides: 173.9 mg/dL; type=numeric |  | observations.csv |
| 2017-04-14 20:51:21 | Lab Results | Urea Nitrogen: 19.1 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=126.37 | **DIABETES** | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=13.40 | **HYPERTENSION** | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=136.53 |  | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=65.37 |  | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=321.34 | **DIABETES** | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=50.12 |  | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=23.94 |  | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=162.95 |  | medications.csv |
| 2017-04-14 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=102.95 |  | medications.csv |
| 2017-05-19 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2017-05-19T21:06:21Z |  | encounters.csv |
| 2017-05-26 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-05-26T21:21:21Z |  | encounters.csv |
| 2017-05-26 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Calcium: 8.6 mg/dL; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Carbon Dioxide: 23.8 mmol/L; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Chloride: 105.0 mmol/L; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Creatinine: 6.3 mg/dL; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Diastolic Blood Pressure: 103.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 15.8 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Glucose: 102.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Heart rate: 99.0 /min; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 50.2 mg/dL; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 131.8 mg/dL; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 128.3 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Potassium: 4.6 mmol/L; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Sodium: 138.4 mmol/L; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Systolic Blood Pressure: 182.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Total Cholesterol: 214.8 mg/dL; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Triglycerides: 164.0 mg/dL; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Lab Results | Urea Nitrogen: 11.3 mg/dL; type=numeric |  | observations.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=122.13 | **DIABETES** | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=28.62 | **HYPERTENSION** | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=88.00 |  | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=36.18 |  | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1284.36 | **DIABETES** | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=100.88 |  | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=32.39 |  | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=155.48 |  | medications.csv |
| 2017-05-26 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=16.59 |  | medications.csv |
| 2017-06-16 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-06-16T21:21:21Z |  | encounters.csv |
| 2017-06-16 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Carbon Dioxide: 21.6 mmol/L; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Chloride: 102.0 mmol/L; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Creatinine: 4.6 mg/dL; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Diastolic Blood Pressure: 101.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 21.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Glucose: 102.1 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Heart rate: 94.0 /min; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 50.4 mg/dL; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 122.7 mg/dL; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 112.5 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Sodium: 138.5 mmol/L; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Systolic Blood Pressure: 156.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Total Cholesterol: 210.9 mg/dL; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Triglycerides: 189.0 mg/dL; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Lab Results | Urea Nitrogen: 15.0 mg/dL; type=numeric |  | observations.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=149.70 | **DIABETES** | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=43.96 | **HYPERTENSION** | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=73.27 |  | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=39.23 |  | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=415.50 | **DIABETES** | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=224.89 |  | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=31.57 |  | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=228.66 |  | medications.csv |
| 2017-06-16 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=109.77 |  | medications.csv |
| 2017-07-14 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2017-07-14T21:06:21Z |  | encounters.csv |
| 2017-07-21 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-07-21T21:21:21Z |  | encounters.csv |
| 2017-07-21 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Carbon Dioxide: 25.6 mmol/L; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Chloride: 108.2 mmol/L; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Creatinine: 5.9 mg/dL; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Diastolic Blood Pressure: 116.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.7 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Glucose: 108.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Heart rate: 61.0 /min; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 54.6 mg/dL; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 137.6 mg/dL; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 211.9 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Potassium: 4.6 mmol/L; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Sodium: 137.3 mmol/L; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Systolic Blood Pressure: 149.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Total Cholesterol: 222.8 mg/dL; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Triglycerides: 153.5 mg/dL; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Lab Results | Urea Nitrogen: 19.7 mg/dL; type=numeric |  | observations.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=81.50 | **DIABETES** | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=67.09 | **HYPERTENSION** | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=77.00 |  | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=31.24 |  | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=757.24 | **DIABETES** | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=39.45 |  | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=44.36 |  | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=126.49 |  | medications.csv |
| 2017-07-21 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=121.28 |  | medications.csv |
| 2017-08-11 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-08-11T21:21:21Z |  | encounters.csv |
| 2017-08-11 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Carbon Dioxide: 23.0 mmol/L; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Chloride: 104.9 mmol/L; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Creatinine: 3.6 mg/dL; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Diastolic Blood Pressure: 117.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 27.6 mL/min/{1.73_m2}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Glucose: 119.9 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Heart rate: 72.0 /min; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 48.1 mg/dL; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 151.0 mg/dL; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 79.1 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Potassium: 4.1 mmol/L; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Sodium: 137.3 mmol/L; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Systolic Blood Pressure: 193.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Total Cholesterol: 232.4 mg/dL; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Triglycerides: 166.3 mg/dL; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Lab Results | Urea Nitrogen: 12.1 mg/dL; type=numeric |  | observations.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=438.76 | **DIABETES** | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=4; total cost=134.00 | **HYPERTENSION** | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=4; total cost=221.40 |  | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=265.12 |  | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=5493.48 | **DIABETES** | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=4; total cost=287.00 |  | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=4; total cost=86.60 |  | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=388.96 |  | medications.csv |
| 2017-08-11 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=84.88 |  | medications.csv |
| 2017-11-10 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2017-11-10T21:06:21Z |  | encounters.csv |
| 2017-12-15 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2017-12-15T21:06:21Z |  | encounters.csv |
| 2017-12-22 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2017-12-22T21:21:21Z |  | encounters.csv |
| 2017-12-22 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Calcium: 8.6 mg/dL; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Carbon Dioxide: 24.4 mmol/L; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Chloride: 102.9 mmol/L; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Creatinine: 3.6 mg/dL; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Diastolic Blood Pressure: 103.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 27.0 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Glucose: 105.7 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Heart rate: 63.0 /min; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 46.2 mg/dL; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 142.3 mg/dL; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 216.5 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Potassium: 5.0 mmol/L; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Sodium: 142.3 mmol/L; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Systolic Blood Pressure: 193.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Total Cholesterol: 221.0 mg/dL; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Triglycerides: 162.5 mg/dL; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Lab Results | Urea Nitrogen: 8.2 mg/dL; type=numeric |  | observations.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=147.02 | **DIABETES** | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=95.02 | **HYPERTENSION** | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=82.62 |  | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=174.38 |  | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=975.26 | **DIABETES** | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=56.02 |  | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=63.14 |  | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=327.04 |  | medications.csv |
| 2017-12-22 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=223.34 |  | medications.csv |
| 2018-02-09 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-02-09T21:06:21Z |  | encounters.csv |
| 2018-02-14 20:51:21 | Lab Results | DALY: 30.2 a; type=numeric |  | observations.csv |
| 2018-02-14 20:51:21 | Lab Results | QALY: 45.8 a; type=numeric |  | observations.csv |
| 2018-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2018-03-09T21:21:21Z |  | encounters.csv |
| 2018-03-09 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Calcium: 9.5 mg/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Carbon Dioxide: 21.4 mmol/L; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Chloride: 108.8 mmol/L; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Creatinine: 3.4 mg/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Diastolic Blood Pressure: 102.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Erythrocyte distribution width [Entitic volume] by Automated count: 39.8 fL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Erythrocytes [#/volume] in Blood by Automated count: 4.9 10*6/uL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 28.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Glucose: 119.9 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Heart rate: 80.0 /min; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Hematocrit [Volume Fraction] of Blood by Automated count: 47.7 %; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Hemoglobin [Mass/volume] in Blood: 14.3 g/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 58.6 mg/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Leukocytes [#/volume] in Blood by Automated count: 5.0 10*3/uL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 140.9 mg/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | MCH [Entitic mass] by Automated count: 31.6 pg; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | MCHC [Mass/volume] by Automated count: 35.0 g/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | MCV [Entitic volume] by Automated count: 90.0 fL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 92.3 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Platelet distribution width [Entitic volume] in Blood by Automated count: 289.3 fL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Platelet mean volume [Entitic volume] in Blood by Automated count: 11.8 fL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Platelets [#/volume] in Blood by Automated count: 164.8 10*3/uL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Potassium: 4.5 mmol/L; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Sodium: 139.6 mmol/L; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Systolic Blood Pressure: 183.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Total Cholesterol: 238.4 mg/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Triglycerides: 194.2 mg/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Lab Results | Urea Nitrogen: 12.0 mg/dL; type=numeric |  | observations.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=4; total cost=803.12 | **DIABETES** | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=4; total cost=1053.96 | **HYPERTENSION** | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=4; total cost=298.08 | **HYPERTENSION** | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=4; total cost=99.32 |  | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=4; total cost=89.16 |  | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=4; total cost=444.60 | **DIABETES** | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=4; total cost=717.68 |  | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=4; total cost=17.28 |  | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=4; total cost=506.44 |  | medications.csv |
| 2018-03-09 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=4; total cost=197.20 |  | medications.csv |
| 2018-03-16 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-03-16T21:06:21Z |  | encounters.csv |
| 2018-04-13 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-04-13T21:06:21Z |  | encounters.csv |
| 2018-05-11 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-05-11T21:06:21Z |  | encounters.csv |
| 2018-06-08 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-06-08T21:06:21Z |  | encounters.csv |
| 2018-06-15 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-06-15T21:06:21Z |  | encounters.csv |
| 2018-07-13 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-07-13T21:06:21Z |  | encounters.csv |
| 2018-07-20 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2018-07-20T21:21:21Z |  | encounters.csv |
| 2018-07-20 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Calcium: 9.3 mg/dL; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Carbon Dioxide: 25.4 mmol/L; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Chloride: 105.4 mmol/L; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Creatinine: 3.6 mg/dL; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Diastolic Blood Pressure: 108.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 26.9 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Glucose: 102.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Heart rate: 93.0 /min; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 57.9 mg/dL; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 143.4 mg/dL; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 179.6 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Potassium: 4.8 mmol/L; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Sodium: 144.0 mmol/L; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Systolic Blood Pressure: 174.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Total Cholesterol: 238.5 mg/dL; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Triglycerides: 186.3 mg/dL; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Lab Results | Urea Nitrogen: 10.3 mg/dL; type=numeric |  | observations.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=147.95 | **DIABETES** | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=23.87 | **HYPERTENSION** | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=81.74 |  | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=85.12 |  | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1599.41 | **DIABETES** | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=129.69 |  | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=44.13 |  | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=26.41 |  | medications.csv |
| 2018-07-20 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=153.64 |  | medications.csv |
| 2018-08-10 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-08-10T21:06:21Z |  | encounters.csv |
| 2018-08-17 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2018-08-17T21:21:21Z |  | encounters.csv |
| 2018-08-17 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Calcium: 10.0 mg/dL; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Carbon Dioxide: 24.2 mmol/L; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Chloride: 110.6 mmol/L; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Creatinine: 5.3 mg/dL; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Diastolic Blood Pressure: 105.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 18.3 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Glucose: 121.2 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Heart rate: 86.0 /min; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 47.7 mg/dL; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 133.6 mg/dL; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 48.2 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 0.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Potassium: 3.9 mmol/L; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Sodium: 136.1 mmol/L; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Systolic Blood Pressure: 171.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Total Cholesterol: 218.7 mg/dL; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Triglycerides: 187.2 mg/dL; type=numeric |  | observations.csv |
| 2018-08-17 20:51:21 | Lab Results | Urea Nitrogen: 16.6 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=191.27 | **DIABETES** | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=7.53 | **HYPERTENSION** | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=102.01 |  | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=35.69 |  | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=210.78 | **DIABETES** | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=194.33 |  | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=4.64 |  | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=118.25 |  | medications.csv |
| 2018-08-17 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=129.92 |  | medications.csv |
| 2018-09-07 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2018-09-07T21:21:21Z |  | encounters.csv |
| 2018-09-07 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Calcium: 10.0 mg/dL; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Carbon Dioxide: 20.9 mmol/L; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Chloride: 108.9 mmol/L; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Creatinine: 3.7 mg/dL; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Diastolic Blood Pressure: 104.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 25.9 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Glucose: 103.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Heart rate: 80.0 /min; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 53.7 mg/dL; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 154.6 mg/dL; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 225.5 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 4.0 {score}; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Sodium: 142.6 mmol/L; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Systolic Blood Pressure: 166.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Total Cholesterol: 238.8 mg/dL; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Triglycerides: 152.7 mg/dL; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Lab Results | Urea Nitrogen: 14.5 mg/dL; type=numeric |  | observations.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=331.05 | **DIABETES** | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=12.29 | **HYPERTENSION** | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=53.46 |  | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=93.80 |  | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=482.32 | **DIABETES** | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=15.97 |  | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=17.07 |  | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=178.60 |  | medications.csv |
| 2018-09-07 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=194.27 |  | medications.csv |
| 2018-10-05 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2018-10-05T21:21:21Z |  | encounters.csv |
| 2018-10-05 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Carbon Dioxide: 22.7 mmol/L; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Chloride: 102.9 mmol/L; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Creatinine: 5.4 mg/dL; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Diastolic Blood Pressure: 104.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 17.9 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Glucose: 120.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Heart rate: 89.0 /min; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 57.6 mg/dL; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 123.1 mg/dL; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 166.1 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 0.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Potassium: 4.1 mmol/L; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Sodium: 139.1 mmol/L; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Systolic Blood Pressure: 199.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Total Cholesterol: 220.3 mg/dL; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Triglycerides: 198.1 mg/dL; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Lab Results | Urea Nitrogen: 8.5 mg/dL; type=numeric |  | observations.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=5; total cost=123.40 | **DIABETES** | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=5; total cost=1317.45 | **HYPERTENSION** | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=5; total cost=165.00 | **HYPERTENSION** | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=5; total cost=167.20 |  | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=5; total cost=333.90 |  | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=5; total cost=3221.55 | **DIABETES** | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=5; total cost=953.30 |  | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=5; total cost=61.70 |  | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=5; total cost=264.70 |  | medications.csv |
| 2018-10-05 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=5; total cost=213.60 |  | medications.csv |
| 2018-11-09 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-11-09T21:06:21Z |  | encounters.csv |
| 2018-12-07 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2018-12-07T21:06:21Z |  | encounters.csv |
| 2019-01-04 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-01-04T21:06:21Z |  | encounters.csv |
| 2019-01-11 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-01-11T21:06:21Z |  | encounters.csv |
| 2019-02-08 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-02-08T21:06:21Z |  | encounters.csv |
| 2019-02-14 20:51:21 | Lab Results | DALY: 30.7 a; type=numeric |  | observations.csv |
| 2019-02-14 20:51:21 | Lab Results | QALY: 46.3 a; type=numeric |  | observations.csv |
| 2019-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2019-03-08 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-03-08T21:06:21Z |  | encounters.csv |
| 2019-03-15 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2019-03-15T21:21:21Z |  | encounters.csv |
| 2019-03-15 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Calcium: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Carbon Dioxide: 25.4 mmol/L; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Chloride: 107.1 mmol/L; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Creatinine: 3.5 mg/dL; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Diastolic Blood Pressure: 119.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 27.1 mL/min/{1.73_m2}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Glucose: 118.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Heart rate: 82.0 /min; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 40.1 mg/dL; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 122.0 mg/dL; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 239.0 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Potassium: 5.0 mmol/L; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Sodium: 142.7 mmol/L; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Systolic Blood Pressure: 139.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Total Cholesterol: 201.7 mg/dL; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Triglycerides: 198.1 mg/dL; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Lab Results | Urea Nitrogen: 10.7 mg/dL; type=numeric |  | observations.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=148.48 | **DIABETES** | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=69.92 | **HYPERTENSION** | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=69.35 |  | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=27.08 |  | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1420.96 | **DIABETES** | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=85.76 |  | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=3.41 |  | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=184.45 |  | medications.csv |
| 2019-03-15 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=157.11 |  | medications.csv |
| 2019-03-22 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-03-22T21:06:21Z |  | encounters.csv |
| 2019-03-30 00:00:00 | Diagnoses | Acute bronchitis (disorder) code=10509002; recorded stop=2019-04-13 |  | conditions.csv |
| 2019-03-30 20:51:21 | Encounters | Encounter for symptom; class=ambulatory; reason=Acute bronchitis (disorder); end=2019-03-30T21:29:21Z |  | encounters.csv |
| 2019-03-30 20:51:21 | Medications Started | Acetaminophen 325 MG Oral Tablet code=313782; reason=Acute bronchitis (disorder); dispenses=1; total cost=5.80 |  | medications.csv |
| 2019-04-05 20:51:21 | Encounters | Emergency Encounter; class=emergency; end=2019-04-05T22:06:21Z |  | encounters.csv |
| 2019-04-12 20:51:21 | Encounters | Emergency Encounter; class=emergency; end=2019-04-12T22:06:21Z |  | encounters.csv |
| 2019-04-13 20:51:21 | Medication Changes | Stopped/ended: Acetaminophen 325 MG Oral Tablet code=313782; reason=Acute bronchitis (disorder) | **MEDICATION CHANGE** | medications.csv |
| 2019-04-19 20:51:21 | Encounters | Emergency Encounter; class=emergency; end=2019-04-19T22:06:21Z |  | encounters.csv |
| 2019-05-03 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2019-05-03T21:21:21Z |  | encounters.csv |
| 2019-05-03 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Carbon Dioxide: 25.9 mmol/L; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Chloride: 102.3 mmol/L; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Creatinine: 3.7 mg/dL; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Diastolic Blood Pressure: 114.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 25.7 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Glucose: 116.0 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Heart rate: 83.0 /min; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 54.0 mg/dL; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 125.4 mg/dL; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 41.1 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Potassium: 3.8 mmol/L; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Sodium: 139.7 mmol/L; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Systolic Blood Pressure: 190.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Total Cholesterol: 215.8 mg/dL; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Triglycerides: 182.2 mg/dL; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Lab Results | Urea Nitrogen: 15.0 mg/dL; type=numeric |  | observations.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=19.01 | **DIABETES** | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=12.07 | **HYPERTENSION** | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=143.73 |  | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=62.07 |  | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=878.97 | **DIABETES** | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=45.81 |  | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=45.97 |  | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=113.17 |  | medications.csv |
| 2019-05-03 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=19.18 |  | medications.csv |
| 2019-06-07 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-06-07T21:06:21Z |  | encounters.csv |
| 2019-06-14 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2019-06-14T21:21:21Z |  | encounters.csv |
| 2019-06-14 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Calcium: 9.5 mg/dL; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Carbon Dioxide: 24.6 mmol/L; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Chloride: 102.3 mmol/L; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Creatinine: 5.1 mg/dL; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Diastolic Blood Pressure: 121.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 18.7 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Glucose: 119.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Heart rate: 92.0 /min; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 47.1 mg/dL; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 130.2 mg/dL; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 84.5 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 0.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Potassium: 5.2 mmol/L; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Sodium: 136.7 mmol/L; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Systolic Blood Pressure: 160.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Total Cholesterol: 217.0 mg/dL; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Triglycerides: 198.3 mg/dL; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Lab Results | Urea Nitrogen: 9.4 mg/dL; type=numeric |  | observations.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=211.27 | **DIABETES** | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=69.34 | **HYPERTENSION** | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=110.87 |  | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=140.39 |  | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=766.56 | **DIABETES** | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=71.84 |  | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=30.93 |  | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=156.58 |  | medications.csv |
| 2019-06-14 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=53.58 |  | medications.csv |
| 2019-07-05 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-07-05T21:06:21Z |  | encounters.csv |
| 2019-07-12 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2019-07-12T21:21:21Z |  | encounters.csv |
| 2019-07-12 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Calcium: 8.8 mg/dL; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Carbon Dioxide: 25.3 mmol/L; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Chloride: 108.7 mmol/L; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Creatinine: 3.6 mg/dL; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Diastolic Blood Pressure: 115.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 26.2 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Glucose: 124.9 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Heart rate: 99.0 /min; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 42.8 mg/dL; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 138.4 mg/dL; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 31.0 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 0.0 {score}; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Potassium: 4.8 mmol/L; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Sodium: 141.0 mmol/L; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Systolic Blood Pressure: 185.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Total Cholesterol: 211.6 mg/dL; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Triglycerides: 152.1 mg/dL; type=numeric |  | observations.csv |
| 2019-07-12 20:51:21 | Lab Results | Urea Nitrogen: 18.4 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=160.02 | **DIABETES** | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=63.45 | **HYPERTENSION** | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=37.60 |  | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=48.34 |  | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=422.19 | **DIABETES** | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=305.51 |  | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=46.09 |  | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=127.73 |  | medications.csv |
| 2019-07-12 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=66.42 |  | medications.csv |
| 2019-08-02 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2019-08-02T21:21:21Z |  | encounters.csv |
| 2019-08-02 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Calcium: 9.5 mg/dL; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Carbon Dioxide: 22.4 mmol/L; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Chloride: 102.8 mmol/L; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Creatinine: 3.4 mg/dL; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Diastolic Blood Pressure: 90.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 28.4 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Glucose: 111.6 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Heart rate: 93.0 /min; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 53.6 mg/dL; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 141.6 mg/dL; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 163.7 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Potassium: 4.3 mmol/L; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Sodium: 136.5 mmol/L; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Systolic Blood Pressure: 178.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Total Cholesterol: 232.8 mg/dL; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Triglycerides: 188.3 mg/dL; type=numeric |  | observations.csv |
| 2019-08-02 20:51:21 | Lab Results | Urea Nitrogen: 8.8 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=253.94 | **DIABETES** | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=11.90 | **HYPERTENSION** | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=169.82 |  | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=241.48 |  | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=2973.28 | **DIABETES** | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=339.94 |  | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=29.36 |  | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=416.40 |  | medications.csv |
| 2019-08-02 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=125.58 |  | medications.csv |
| 2019-09-06 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-09-06T21:06:21Z |  | encounters.csv |
| 2019-10-04 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2019-10-04T21:21:21Z |  | encounters.csv |
| 2019-10-04 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Calcium: 9.8 mg/dL; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Carbon Dioxide: 21.2 mmol/L; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Chloride: 104.4 mmol/L; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Creatinine: 4.6 mg/dL; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Diastolic Blood Pressure: 102.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 20.7 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Glucose: 117.6 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Heart rate: 68.0 /min; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 58.3 mg/dL; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 108.6 mg/dL; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 88.3 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Potassium: 4.4 mmol/L; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Respiratory rate: 16.0 /min; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Sodium: 142.0 mmol/L; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Systolic Blood Pressure: 155.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Total Cholesterol: 204.4 mg/dL; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Triglycerides: 187.3 mg/dL; type=numeric |  | observations.csv |
| 2019-10-04 20:51:21 | Lab Results | Urea Nitrogen: 13.8 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=299.17 | **DIABETES** | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=22.80 | **HYPERTENSION** | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=55.70 |  | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=11.88 |  | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=768.05 | **DIABETES** | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=308.28 |  | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=27.12 |  | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=20.92 |  | medications.csv |
| 2019-10-04 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=128.30 |  | medications.csv |
| 2019-11-01 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-11-01T21:06:21Z |  | encounters.csv |
| 2019-11-08 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2019-11-08T21:21:21Z |  | encounters.csv |
| 2019-11-08 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Calcium: 9.9 mg/dL; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Carbon Dioxide: 27.3 mmol/L; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Chloride: 107.9 mmol/L; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Creatinine: 5.8 mg/dL; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Diastolic Blood Pressure: 98.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 16.6 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Glucose: 119.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Heart rate: 88.0 /min; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 48.2 mg/dL; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 133.8 mg/dL; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 206.5 mg/g; type=numeric | **DIABETES** **SIGNIFICANT CHANGE** | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 1.0 {score}; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Potassium: 3.8 mmol/L; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Respiratory rate: 13.0 /min; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Sodium: 143.8 mmol/L; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Systolic Blood Pressure: 140.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Total Cholesterol: 214.3 mg/dL; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Triglycerides: 161.2 mg/dL; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Lab Results | Urea Nitrogen: 9.9 mg/dL; type=numeric |  | observations.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=353.38 | **DIABETES** | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=9.00 | **HYPERTENSION** | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=33.14 |  | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=42.81 |  | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=462.85 | **DIABETES** | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=29.40 |  | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=41.31 |  | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=13.19 |  | medications.csv |
| 2019-11-08 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=33.47 |  | medications.csv |
| 2019-11-29 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2019-11-29T21:06:21Z |  | encounters.csv |
| 2019-12-06 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2019-12-06T21:21:21Z |  | encounters.csv |
| 2019-12-06 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Calcium: 9.6 mg/dL; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Carbon Dioxide: 24.0 mmol/L; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Chloride: 106.0 mmol/L; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Creatinine: 4.1 mg/dL; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Diastolic Blood Pressure: 109.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.1 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Glucose: 104.4 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Heart rate: 92.0 /min; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 40.2 mg/dL; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 153.6 mg/dL; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 279.0 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 2.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Sodium: 143.7 mmol/L; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Systolic Blood Pressure: 191.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Total Cholesterol: 230.1 mg/dL; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Triglycerides: 181.4 mg/dL; type=numeric |  | observations.csv |
| 2019-12-06 20:51:21 | Lab Results | Urea Nitrogen: 15.3 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=184.08 | **DIABETES** | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=46.62 | **HYPERTENSION** | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=20.37 |  | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=48.61 |  | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=976.25 | **DIABETES** | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=185.19 |  | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=5.92 |  | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=209.14 |  | medications.csv |
| 2019-12-06 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=202.54 |  | medications.csv |
| 2020-01-03 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2020-01-03T21:06:21Z |  | encounters.csv |
| 2020-01-10 20:51:21 | Encounters | Encounter for check up (procedure); class=outpatient; end=2020-01-10T21:21:21Z |  | encounters.csv |
| 2020-01-10 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Calcium: 9.0 mg/dL; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Carbon Dioxide: 22.1 mmol/L; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Chloride: 106.2 mmol/L; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Creatinine: 3.9 mg/dL; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Diastolic Blood Pressure: 109.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 24.3 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Glucose: 123.5 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Heart rate: 93.0 /min; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 57.4 mg/dL; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 114.4 mg/dL; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 218.9 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Potassium: 5.1 mmol/L; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Respiratory rate: 14.0 /min; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Sodium: 140.6 mmol/L; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Systolic Blood Pressure: 156.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Total Cholesterol: 203.8 mg/dL; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Triglycerides: 160.2 mg/dL; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Lab Results | Urea Nitrogen: 15.0 mg/dL; type=numeric |  | observations.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=2; total cost=218.56 | **DIABETES** | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=2; total cost=526.98 | **HYPERTENSION** | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=2; total cost=48.66 | **HYPERTENSION** | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=2; total cost=39.74 |  | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=2; total cost=142.30 |  | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=2; total cost=946.02 | **DIABETES** | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=2; total cost=327.50 |  | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=2; total cost=31.16 |  | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=2; total cost=220.72 |  | medications.csv |
| 2020-01-10 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=2; total cost=84.34 |  | medications.csv |
| 2020-01-31 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2020-01-31T21:06:21Z |  | encounters.csv |
| 2020-02-14 20:51:21 | Lab Results | DALY: 31.2 a; type=numeric |  | observations.csv |
| 2020-02-14 20:51:21 | Lab Results | QALY: 46.8 a; type=numeric |  | observations.csv |
| 2020-02-14 20:51:21 | Lab Results | QOLS: 0.5 {score}; type=numeric |  | observations.csv |
| 2020-02-28 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2020-02-28T21:06:21Z |  | encounters.csv |
| 2020-03-20 20:51:21 | Encounters | General examination of patient (procedure); class=wellness; end=2020-03-20T21:36:21Z |  | encounters.csv |
| 2020-03-20 20:51:21 | Lab Results | Body Height: 163.8 cm; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Body Mass Index: 48.5 kg/m2; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Body Weight: 130.2 kg; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Calcium: 9.2 mg/dL; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Carbon Dioxide: 25.0 mmol/L; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Chloride: 107.1 mmol/L; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Creatinine: 4.1 mg/dL; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Diastolic Blood Pressure: 111.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Estimated Glomerular Filtration Rate: 23.1 mL/min/{1.73_m2}; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Glucose: 112.6 mg/dL; type=numeric | **DIABETES** | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Heart rate: 95.0 /min; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Hemoglobin A1c/Hemoglobin.total in Blood: 4.5 %; type=numeric | **DIABETES** | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | High Density Lipoprotein Cholesterol: 54.6 mg/dL; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Low Density Lipoprotein Cholesterol: 136.9 mg/dL; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Microalbumin Creatinine Ratio: 235.6 mg/g; type=numeric | **DIABETES** | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Pain severity - 0-10 verbal numeric rating [Score] - Reported: 3.0 {score}; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Potassium: 4.2 mmol/L; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Respiratory rate: 15.0 /min; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Sodium: 139.8 mmol/L; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Systolic Blood Pressure: 175.0 mm[Hg]; type=numeric | **HYPERTENSION** | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Tobacco smoking status NHIS: Never smoker ; type=text |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Total Cholesterol: 221.9 mg/dL; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Triglycerides: 151.9 mg/dL; type=numeric |  | observations.csv |
| 2020-03-20 20:51:21 | Lab Results | Urea Nitrogen: 7.2 mg/dL; type=numeric |  **SIGNIFICANT CHANGE** | observations.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Amlodipine 5 MG Oral Tablet code=197361 | **HYPERTENSION** **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Clopidogrel 75 MG Oral Tablet code=309362 | **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Digoxin 0.125 MG Oral Tablet code=197604 | **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes | **DIABETES** **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129 | **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Simvastatin 20 MG Oral Tablet code=312961 | **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Verapamil Hydrochloride 40 MG code=897718 | **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medication Changes | Stopped/ended: Warfarin Sodium 5 MG Oral Tablet code=855332 | **MEDICATION CHANGE** | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet code=860975; reason=Diabetes; dispenses=1; total cost=274.24 | **DIABETES** | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet code=999967; reason=Hypertension; dispenses=1; total cost=263.49 | **HYPERTENSION** | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Amlodipine 5 MG Oral Tablet code=197361; dispenses=1; total cost=20.35 | **HYPERTENSION** | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Clopidogrel 75 MG Oral Tablet code=309362; dispenses=1; total cost=137.81 |  | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Digoxin 0.125 MG Oral Tablet code=197604; dispenses=1; total cost=56.89 |  | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] code=865098; reason=Diabetes; dispenses=1; total cost=1468.17 | **DIABETES** | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray code=705129; dispenses=1; total cost=181.23 |  | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Simvastatin 20 MG Oral Tablet code=312961; dispenses=1; total cost=40.32 |  | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Verapamil Hydrochloride 40 MG code=897718; dispenses=1; total cost=51.35 |  | medications.csv |
| 2020-03-20 20:51:21 | Medications Started | Warfarin Sodium 5 MG Oral Tablet code=855332; dispenses=1; total cost=68.76 |  | medications.csv |
| 2020-04-03 20:51:21 | Encounters | Urgent care clinic (procedure); class=urgentcare; end=2020-04-03T21:06:21Z |  | encounters.csv |

# B. Condensed Clinical Summary

## Longitudinal Profile

- **367** encounters across **72.7 years**.
- Encounter classes: outpatient (195); urgentcare (95); wellness (63); ambulatory (8); emergency (6).

## Diagnoses

| Start | Stop | Diagnosis | Highlights |
| --- | --- | --- | --- |
| 1947-08-08 |  | Cardiac Arrest |  |
| 1947-08-08 |  | History of cardiac arrest (situation) |  |
| 1956-03-23 |  | Body mass index 30+ - obesity (finding) |  |
| 1957-03-29 |  | Body mass index 40+ - severely obese (finding) |  |
| 1959-04-10 |  | Hypertension | **HYPERTENSION** |
| 1969-06-06 |  | Anemia (disorder) |  |
| 1969-06-06 |  | Diabetes | **DIABETES** |
| 1970-06-12 |  | Hypertriglyceridemia (disorder) |  |
| 1970-06-12 |  | Metabolic syndrome X (disorder) |  |
| 1971-06-18 |  | Hyperglycemia (disorder) | **DIABETES** |
| 1980-08-08 |  | Neuropathy due to type 2 diabetes mellitus (disorder) | **DIABETES** |
| 1982-03-19 |  | Chronic kidney disease stage 1 (disorder) |  |
| 1982-03-19 |  | Diabetic renal disease (disorder) | **DIABETES** |
| 1996-05-03 |  | Atrial Fibrillation |  |
| 2009-05-01 |  | Coronary Heart Disease |  |
| 2010-12-16 | 2010-12-28 | Acute viral pharyngitis (disorder) |  |
| 2011-12-13 | 2011-12-20 | Acute bronchitis (disorder) |  |
| 2014-02-21 | 2014-04-11 | Otitis media |  |
| 2015-06-06 | 2015-06-27 | Viral sinusitis (disorder) |  |
| 2016-10-13 | 2017-01-11 | Fracture of forearm |  |
| 2019-03-30 | 2019-04-13 | Acute bronchitis (disorder) |  |

## Major Medication Patterns

Grouped from all medication rows; record count reflects repeated prescriptions/dispenses.

| Medication | Records | First start | Last start | Reasons | Highlights |
| --- | ---: | --- | --- | --- | --- |
| amLODIPine 5 MG / Hydrochlorothiazide 12.5 MG / Olmesartan medoxomil 20 MG Oral Tablet | 258 | 1959-07-09T20:51:21Z | 2020-03-20T20:51:21Z | Hypertension | **HYPERTENSION** |
| 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | 248 | 1969-06-06T20:51:21Z | 2020-03-20T20:51:21Z | Diabetes | **DIABETES** |
| Insulin Lispro 100 UNT/ML Injectable Solution [Humalog] | 232 | 1982-10-15T20:51:21Z | 2020-03-20T20:51:21Z | Diabetes | **DIABETES** |
| Digoxin 0.125 MG Oral Tablet | 172 | 1996-05-03T20:51:21Z | 2020-03-20T20:51:21Z |  |  |
| Verapamil Hydrochloride 40 MG | 172 | 1996-05-03T20:51:21Z | 2020-03-20T20:51:21Z |  |  |
| Warfarin Sodium 5 MG Oral Tablet | 172 | 1996-05-03T20:51:21Z | 2020-03-20T20:51:21Z |  |  |
| Amlodipine 5 MG Oral Tablet | 76 | 2009-05-01T20:51:21Z | 2020-03-20T20:51:21Z |  | **HYPERTENSION** |
| Clopidogrel 75 MG Oral Tablet | 76 | 2009-05-01T20:51:21Z | 2020-03-20T20:51:21Z |  |  |
| Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | 76 | 2009-05-01T20:51:21Z | 2020-03-20T20:51:21Z |  |  |
| Simvastatin 20 MG Oral Tablet | 76 | 2009-05-01T20:51:21Z | 2020-03-20T20:51:21Z |  |  |
| Acetaminophen 325 MG Oral Tablet | 4 | 2011-12-13T20:51:21Z | 2019-03-30T20:51:21Z | Acute bronchitis (disorder) |  |
| Acetaminophen 325 MG / HYDROcodone Bitartrate 7.5 MG Oral Tablet | 1 | 2016-10-13T20:51:21Z | 2016-10-13T20:51:21Z |  |  |

## Key Lab and Measurement Trends

| Type | Results | First | Latest | Minimum | Maximum | Highlights |
| --- | ---: | --- | --- | --- | --- | --- |
| Creatinine | 65 | 2010-05-28T20:51:21Z: 6.0 mg/dL | 2020-03-20T20:51:21Z: 4.1 mg/dL | 3.4 | 6.7 |  |
| Diastolic Blood Pressure | 65 | 2010-05-28T20:51:21Z: 117.0 mm[Hg] | 2020-03-20T20:51:21Z: 111.0 mm[Hg] | 90 | 121 | **HYPERTENSION** |
| Estimated Glomerular Filtration Rate | 65 | 2010-05-28T20:51:21Z: 17.7 mL/min/{1.73_m2} | 2020-03-20T20:51:21Z: 23.1 mL/min/{1.73_m2} | 15.4 | 28.6 |  |
| Glucose | 65 | 2010-05-28T20:51:21Z: 105.1 mg/dL | 2020-03-20T20:51:21Z: 112.6 mg/dL | 100.6 | 124.9 | **DIABETES** |
| Hemoglobin A1c/Hemoglobin.total in Blood | 65 | 2010-05-28T20:51:21Z: 4.4 % | 2020-03-20T20:51:21Z: 4.5 % | 3.5 | 4.5 | **DIABETES** |
| High Density Lipoprotein Cholesterol | 65 | 2010-05-28T20:51:21Z: 46.4 mg/dL | 2020-03-20T20:51:21Z: 54.6 mg/dL | 40.1 | 58.6 |  |
| Low Density Lipoprotein Cholesterol | 65 | 2010-05-28T20:51:21Z: 141.9 mg/dL | 2020-03-20T20:51:21Z: 136.9 mg/dL | 108.6 | 162.8 |  |
| Microalbumin Creatinine Ratio | 65 | 2010-05-28T20:51:21Z: 57.7 mg/g | 2020-03-20T20:51:21Z: 235.6 mg/g | 31 | 295.3 | **DIABETES** |
| Systolic Blood Pressure | 65 | 2010-05-28T20:51:21Z: 155.0 mm[Hg] | 2020-03-20T20:51:21Z: 175.0 mm[Hg] | 139 | 199 | **HYPERTENSION** |
| Total Cholesterol | 65 | 2010-05-28T20:51:21Z: 226.4 mg/dL | 2020-03-20T20:51:21Z: 221.9 mg/dL | 200.1 | 239 |  |
| Triglycerides | 65 | 2010-05-28T20:51:21Z: 190.7 mg/dL | 2020-03-20T20:51:21Z: 151.9 mg/dL | 151.9 | 198.4 |  |

## Largest Flagged Numeric Changes

Top 20 by absolute percentage change under the documented >=50% rule.

| Date/time | Observation | Previous | Current | Change |
| --- | --- | --- | --- | ---: |
| 2014-11-07 20:51:21 | Microalbumin Creatinine Ratio | 41.4 mg/g | 223 mg/g | 438.6% |
| 2019-08-02 20:51:21 | Microalbumin Creatinine Ratio | 31 mg/g | 163.7 mg/g | 428.1% |
| 2018-09-07 20:51:21 | Microalbumin Creatinine Ratio | 48.2 mg/g | 225.5 mg/g | 367.8% |
| 2016-11-25 20:51:21 | Microalbumin Creatinine Ratio | 61.5 mg/g | 246.3 mg/g | 300.5% |
| 2015-11-27 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 4 {score} | 300% |
| 2016-11-25 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 4 {score} | 300% |
| 2012-07-13 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 4 {score} | 300% |
| 2014-05-02 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 4 {score} | 300% |
| 2010-08-27 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 4 {score} | 300% |
| 2013-02-08 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 4 {score} | 300% |
| 2012-02-17 20:51:21 | Microalbumin Creatinine Ratio | 93 mg/g | 293.7 mg/g | 215.8% |
| 2017-03-03 20:51:21 | Microalbumin Creatinine Ratio | 56.2 mg/g | 176.9 mg/g | 214.8% |
| 2014-07-11 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 3 {score} | 200% |
| 2017-05-26 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 3 {score} | 200% |
| 2013-12-13 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 3 {score} | 200% |
| 2017-08-11 20:51:21 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | 1 {score} | 3 {score} | 200% |
| 2017-12-22 20:51:21 | Microalbumin Creatinine Ratio | 79.1 mg/g | 216.5 mg/g | 173.7% |
| 2015-02-20 20:51:21 | Microalbumin Creatinine Ratio | 39.6 mg/g | 99.2 mg/g | 150.5% |
| 2019-11-08 20:51:21 | Microalbumin Creatinine Ratio | 88.3 mg/g | 206.5 mg/g | 133.9% |
| 2011-02-25 20:51:21 | Microalbumin Creatinine Ratio | 128.3 mg/g | 295.3 mg/g | 130.2% |

## Medication Changes

- Medication start events: **1563**
- Medication stop/end events: **1553**
- Earliest medication start: **1959-07-09T20:51:21Z**
- Latest medication start: **2020-03-20T20:51:21Z**

