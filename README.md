# NHS Prescribing Real-World Evidence (RWE) Analysis

## Project Overview

This project analyses NHS Prescription Cost Analysis (PCA) data to investigate prescribing patterns and prescribing expenditure across England.

Using Python, the project explores real-world prescribing behaviour through Exploratory Data Analysis (EDA) and Real-World Evidence (RWE) analyses to identify the medicines and British National Formulary (BNF) chapters that drive NHS prescribing activity and costs.

---

## Objectives

The analysis aims to:

* Identify the medicines that contribute most to NHS prescribing expenditure.
* Investigate prescribing volume across medicines and BNF chapters.
* Explore prescribing cost trends across BNF chapters.
* Generate Real-World Evidence (RWE) insights from national NHS prescribing data.

---

## Dataset

Source:

NHS Business Services Authority. "Prescription Cost Analysis (PCA) Monthly Administrative Data.” NHS Business Services Authority Open Data. Accessed **[27/07/2026]**. 
URL: https://opendata.nhsbsa.net/dataset/prescription-cost-analysis-pca-monthly-data

Period analysed:

- January 2026
- February 2026
- March 2026
- April 2026

Due to the dataset size, the raw PCA files are not included in this repository. Processed summary tables and analysis outputs are provided instead.

Note: Analyses and dashboard visualisations were generated using a cleaned NHS PCA dataset with "Exception Handler Unspecified Item" records removed, as these represent non-standard prescribing records and accounted for approximately 0.04% of the dataset.

---

## Project Structure

```
NHS_Prescribing_RWE_Analysis/

├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   └── 03_EDA_Analysis.ipynb
│   └── 04_Real_World_Evidence_Insights.ipynb

│
├── src/
│   └── Plotting_Functions.py
│
├── outputs/
│   ├── figures/
│   └── tables/
│
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Key Outputs

The project includes:

- Data cleaning and preprocessing pipeline
- Exploratory Data Analysis (EDA)
- Reusable plotting functions
- Summary tables
- Publication-quality visualisations
- Real-World Evidence (RWE) analyses

---

## Real-World Evidence (RWE) Questions

The analysis explores the following Real-World Evidence questions using NHS Prescription Cost Analysis (PCA) data:

### Research Question 1: Which products are the key drivers of NHS prescribing expenditure?

**Objective:**  
To identify the products contributing most significantly to NHS prescribing expenditure.

**Analysis:**
- Top 10 products by total Net Ingredient Cost (NIC).
- Top 10 products by prescribing volume (items dispensed).

**Key insight:**  
High NHS prescribing expenditure was concentrated among a small number of products, including advanced therapies and medical technologies while routine medicines used for chronic disease management accounted for the highest prescribing volumes.

---

### Research Question 2: Which BNF chapters account for the greatest NHS prescribing expenditure?

**Objective:**  
To identify the BNF chapters contributing most significantly to NHS prescribing expenditure.

**Analysis:**
- Ranking of BNF chapters by total NIC.
- Distribution of total prescribing expenditure across major BNF chapters.

**Key insight:**  
Prescribing expenditure was concentrated within a small number of therapeutic areas, with the Endocrine System, Central Nervous System, and Respiratory System representing major contributors to NHS prescribing costs.

---

### Research Question 3: How did monthly NHS prescribing expenditure vary across the highest-cost BNF chapters between January and April 2026?

**Objective:**  
- Monthly NHS prescribing expenditure trends (January–April 2026) across the highest-cost BNF chapters.
**Analysis:**
- Monthly prescribing expenditure trends across the top 5 highest-cost BNF chapters.

**Key insight:**  
Prescribing expenditure patterns remained relatively stable between January and April 2026, with the same major therapeutic areas consistently driving NHS prescribing expenditure.

## Future Work

Future work includes extending the analysis with additional Real-World Evidence (RWE) questions, investigating prescribing costs, prescribing trends, and variations across BNF chapters.

Planned extensions include:

* Developing an interactive Tableau dashboard to communicate key findings.
* Incorporating additional PCA monthly data as it becomes available to support longer-term prescribing trend analysis.
* Expanding the analysis to explore further prescribing patterns across therapeutic areas.
