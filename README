# Peruvian Energy Demand Analysis (COES Data)

## Overview
This project is a **master's assignment in Data Science** at **Universidad Católica San Pablo - Arequipa**. It analyzes **Peruvian urban energy consumption data** using publicly available information from the **COES (Comité de Operación Económica del Sistema Interconectado Nacional)**. The goal is to evaluate the **maximum monthly energy demand** and obtain insights on energy usage trends over the years.

Data source: [COES - Evaluación Mensual](https://www.coes.org.pe/Portal/PostOperacion/Informes/EvaluacionMensual)

The analysis pipeline includes:
- Web scraping to collect monthly data automatically.
- Data preprocessing to extract relevant metrics.
- Consolidation of all years’ data into a single CSV for further analysis.


## Files

### 1. `scrapping_coes.py`
- Contains the **web scraping logic** to download monthly energy reports from the COES portal.
- Downloads Excel files from **2018 to the current year**.

### 2. `preprocess.py`
- Processes the downloaded Excel files.
- Extracts maximum energy consumption data per month.
- Creates a **clean CSV** consolidating all years into `df_final.csv`.

### 3. `df_final.csv`
- Contains the final processed data.
- Columns include:
  - `Tipo de Generación` (Type of Energy Generation)
  - `Consumo(MW)` (Maximum Demand in MW)
  - `Mes` (Month)
  - `Año` (Year)

### 4. Notebook (Optional)
- Explains the **data collection process** and includes **initial exploratory data analysis (EDA)**.
- Generates visualizations and basic statistics to better understand energy consumption trends.

---

## Installation / Dependencies

Make sure you have Python 3.x installed.  
Install the required Python libraries:
```bash
pip install pandas beautifulsoup4 requests openpyxl
```

## Steps to Run

1. Run the web scraping script to download data:
```
python scrapping_coes.py
```

2. Preprocess the downloaded files:
```
python preprocess.py
```

3. The final consolidated dataset will be available in df_final.csv.

## Insights

* The data allows tracking maximum energy demand trends over time.
* Can be used to support energy planning or resource allocation.
* Provides a monthly indicator of energy consumption, useful for corporate or urban energy studies.

## Notes

* Only data from 2018 onward is collected.
* Web scraping ensures automatic monthly updates.
* Preprocessing scripts handle Excel files with varying formats and extract only relevant columns.