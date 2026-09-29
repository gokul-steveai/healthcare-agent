# Synthea CSV Dataset Summary

- Source directory: `/home/ayush/Downloads/synthea_sample_data_csv_apr2020/csv`
- Analysis scope: `patients.csv`, `conditions.csv`, `medications.csv`, and `observations.csv`
- Condition cohort rule: case-insensitive exact matches on `conditions.DESCRIPTION` for `Diabetes` and `Hypertension` for the same patient.
- Per-patient totals are row counts in each corresponding CSV across the complete dataset; they are not distinct-description counts.

## Record Counts

| File | Total records |
| --- | --- |
| patients.csv | 1171 |
| conditions.csv | 8376 |
| medications.csv | 42989 |
| observations.csv | 299697 |

## Columns

### patients.csv

`Id`, `BIRTHDATE`, `DEATHDATE`, `SSN`, `DRIVERS`, `PASSPORT`, `PREFIX`, `FIRST`, `LAST`, `SUFFIX`, `MAIDEN`, `MARITAL`, `RACE`, `ETHNICITY`, `GENDER`, `BIRTHPLACE`, `ADDRESS`, `CITY`, `STATE`, `COUNTY`, `ZIP`, `LAT`, `LON`, `HEALTHCARE_EXPENSES`, `HEALTHCARE_COVERAGE`

### conditions.csv

`START`, `STOP`, `PATIENT`, `ENCOUNTER`, `CODE`, `DESCRIPTION`

### medications.csv

`START`, `STOP`, `PATIENT`, `PAYER`, `ENCOUNTER`, `CODE`, `DESCRIPTION`, `BASE_COST`, `PAYER_COVERAGE`, `DISPENSES`, `TOTALCOST`, `REASONCODE`, `REASONDESCRIPTION`

### observations.csv

`DATE`, `PATIENT`, `ENCOUNTER`, `CODE`, `DESCRIPTION`, `VALUE`, `UNITS`, `TYPE`

## Top 20 Conditions by Frequency

| Condition | Frequency |
| --- | --- |
| Viral sinusitis (disorder) | 1248 |
| Acute viral pharyngitis (disorder) | 653 |
| Acute bronchitis (disorder) | 563 |
| Normal pregnancy | 516 |
| Body mass index 30+ - obesity (finding) | 449 |
| Prediabetes | 317 |
| Hypertension | 302 |
| Anemia (disorder) | 300 |
| Chronic sinusitis (disorder) | 236 |
| Miscarriage in first trimester | 221 |
| Otitis media | 196 |
| Streptococcal sore throat (disorder) | 157 |
| Hyperlipidemia | 136 |
| Sprain of ankle | 134 |
| Polyp of colon | 79 |
| Concussion with no loss of consciousness | 77 |
| Diabetes | 76 |
| Hypertriglyceridemia (disorder) | 74 |
| Metabolic syndrome X (disorder) | 74 |
| Acute bacterial sinusitis (disorder) | 69 |

## Top 20 Observation Types by Frequency

| Observation type (`DESCRIPTION`) | Frequency |
| --- | --- |
| Pain severity - 0-10 verbal numeric rating [Score] - Reported | 16820 |
| Diastolic Blood Pressure | 12963 |
| Systolic Blood Pressure | 12963 |
| Body Height | 12552 |
| Body Weight | 12552 |
| Heart rate | 12552 |
| Respiratory rate | 12552 |
| Tobacco smoking status NHIS | 12552 |
| Body Mass Index | 11451 |
| DALY | 10121 |
| QALY | 10121 |
| QOLS | 10121 |
| Calcium | 6515 |
| Carbon Dioxide | 6515 |
| Chloride | 6515 |
| Creatinine | 6515 |
| Glucose | 6515 |
| Potassium | 6515 |
| Sodium | 6515 |
| Urea Nitrogen | 6515 |

## Patients with Both Diabetes and Hypertension

Qualifying patients: **44**

| Patient ID | Gender | Birthdate | Number of conditions | Number of medications | Number of observations |
| --- | --- | --- | --- | --- | --- |
| 02f9aadd-72de-4b20-b381-f4c3b1cf7aa3 | M | 1942-05-23 | 17 | 29 | 463 |
| 0325261f-61eb-46f8-acc6-89d15053fecd | F | 1922-02-14 | 19 | 354 | 1035 |
| 19d2cfb8-439b-454a-b47e-5274c219005b | M | 1914-09-06 | 13 | 1614 | 8560 |
| 1c2d500e-c583-40f8-83a8-c987d21346b7 | F | 1988-02-14 | 18 | 9 | 146 |
| 202b3372-a1d4-42bd-b4b7-b712bd24dc98 | F | 1961-11-12 | 9 | 40 | 292 |
| 2c71dd97-7085-416a-aa07-d675bbe3adf2 | F | 1941-02-14 | 21 | 1563 | 1617 |
| 2d350bad-f546-4799-b04a-32236b4b3930 | F | 1923-05-15 | 13 | 128 | 323 |
| 30d83f4d-837c-488d-9748-5ee0fa49edd5 | M | 1965-12-20 | 11 | 58 | 328 |
| 3acf9313-1874-4dff-ab2a-3187516d92d6 | M | 1917-05-07 | 15 | 1237 | 2655 |
| 3b95da79-b5aa-419a-9558-f4627b02ae3a | M | 1958-12-03 | 17 | 100 | 560 |
| 53f3587e-b9bf-473a-b36e-62f0e1946fa1 | F | 1949-02-26 | 17 | 217 | 1233 |
| 55cc31db-baec-40b5-9b4d-276944000751 | M | 1963-08-07 | 10 | 42 | 304 |
| 5c06120a-9af5-4204-951b-7a8bfc465df3 | F | 1960-01-27 | 22 | 79 | 658 |
| 5dccb2e6-668f-41b4-add4-4020617610b3 | M | 1965-01-02 | 10 | 47 | 277 |
| 64eb57c7-d74d-4f4f-9f7f-b58a1fbc57df | M | 1968-06-06 | 14 | 50 | 365 |
| 6958e2b0-3c19-4217-8049-2d315c70cab5 | M | 1937-02-10 | 17 | 129 | 324 |
| 6ec18ddf-e9ee-421a-9033-456f558c7b4b | M | 1937-02-10 | 25 | 436 | 2184 |
| 714b9c18-783d-4f52-aa64-cc3a05a286d9 | M | 1946-01-22 | 21 | 490 | 1567 |
| 7c6d7838-6453-4e4a-817e-39c8c387f986 | M | 1914-09-06 | 14 | 201 | 1731 |
| 7d61895a-dbf3-472b-9675-421381787295 | F | 1948-03-23 | 16 | 164 | 825 |
| 7f9a57e5-cfc5-4970-b19f-1a7b6ce22882 | F | 1971-09-11 | 8 | 21 | 232 |
| 81805635-f2f4-4844-b71b-73578520d372 | M | 1953-01-20 | 16 | 110 | 544 |
| 8505e011-20cb-4bc5-8a66-5900111fb04b | F | 1960-03-11 | 14 | 92 | 520 |
| 85a0da4b-6e8d-492c-976b-748e39daf4ef | M | 1933-12-19 | 18 | 300 | 540 |
| 87f05059-de42-4630-a35b-edb53d880640 | F | 1922-02-14 | 20 | 90 | 266 |
| 88ea8573-863c-47e3-b144-b810c63156a0 | F | 1962-10-25 | 14 | 149 | 1037 |
| 92408d94-8b50-4e26-a6e1-42ee77823db6 | F | 1979-09-22 | 16 | 25 | 264 |
| 9394cb52-7d92-4577-976e-d017af06ed8f | F | 1980-03-15 | 23 | 14 | 168 |
| 9c4c1885-35af-48b9-a09f-4ea448d40d75 | F | 1922-02-14 | 17 | 482 | 827 |
| 9c90166d-96cb-4680-9190-35ab3e448c53 | M | 1987-02-06 | 10 | 18 | 308 |
| 9e081e53-a748-47c5-8e36-d9c858d23c14 | M | 1939-06-11 | 17 | 200 | 1039 |
| ab6a2662-f6d1-4da6-b3ce-3929d68650d7 | F | 1971-01-16 | 13 | 23 | 253 |
| b118adba-1330-4ba0-8d96-fe610dfbd41e | M | 1966-09-21 | 13 | 89 | 560 |
| b271a454-c57e-4566-899a-956e5484c5e1 | M | 1985-11-06 | 11 | 30 | 393 |
| b75f21c7-f0e8-403c-bef7-e200aba1f573 | F | 1966-09-21 | 10 | 54 | 316 |
| b953a648-a3e3-4d9f-a4be-28e13deaa08f | F | 1986-05-13 | 10 | 13 | 167 |
| be33d994-f841-40a4-9410-66555cf90fed | F | 1969-02-11 | 13 | 47 | 252 |
| c6fc7fe8-483a-4df7-ba2b-260ea4de9aa4 | M | 1963-05-17 | 14 | 46 | 239 |
| cb7b125f-b586-4ed2-9d0c-77f449f39d8b | M | 1965-09-12 | 9 | 123 | 1060 |
| cdef53d5-0537-4073-8874-79fa5e0346e6 | F | 1940-04-05 | 20 | 115 | 574 |
| dac134fa-7f57-4211-923a-e943a5c11d93 | M | 1969-02-26 | 13 | 126 | 920 |
| df7c1d66-eac2-49bd-9d12-ee17e8758f68 | F | 1979-11-19 | 15 | 135 | 176 |
| ea521af0-e6c4-4a3c-899c-89c35c49287d | M | 1954-06-10 | 18 | 367 | 1212 |
| f9149e25-1799-44bf-a5aa-449b41161345 | F | 1981-05-26 | 19 | 172 | 1060 |

