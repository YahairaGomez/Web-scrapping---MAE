# Peruvian Energy Demand Analysis (COES Data)
## 📌 Overview

This project is part of a Master’s assignment in Data Science at Universidad Católica San Pablo - Arequipa. It focuses on analyzing Peruvian urban energy consumption using publicly available data from the COES (Comité de Operación Económica del Sistema Interconectado Nacional).

The main objective is to evaluate the maximum monthly energy demand and generate insights into long-term consumption trends.

A key contribution of this project is the automation of data collection through web scraping. In practice, this represents a major time-saving advantage:

- In many companies (including my own), these monthly reports are usually provided by the Reliability Department at the end of each month.
- However, by automating the data extraction, we can access monthly reports instantly and evaluate in real-time whether the energy-saving proposals implemented are delivering results or not.
- Additionally, manually navigating through multiple folders to find reports is tedious and error-prone. This workflow removes that barrier and makes the process more efficient.

Data source: [COES - Evaluación Mensual](https://www.coes.org.pe/Portal/PostOperacion/Informes/EvaluacionMensual)

## ⚙️ Analysis Pipeline

1. Web Scraping – Downloads monthly Excel reports automatically.
2. Data Preprocessing – Cleans and standardizes data, extracting maximum energy demand per month.
3. Data Consolidation – Combines all years into a single CSV for further analysis.
4. Exploratory Data Analysis (EDA) – Provides initial insights, including seasonal trends and source-specific consumption.

## 📂 Files
1. `scrapping_coes.py`

- Implements the web scraping logic to download monthly reports from COES.
- Saves Excel files into the output_files directory, organized by year.
- Data was collected from 2018 to 2024, since earlier reports follow a different HTML structure.
- ⚠️ Note: COES may change its HTML structure at any time, so this script is designed for the current Post-Operación > Evaluación Mensual section.

2. `preprocess.py`

- Reads all downloaded Excel files.
- Standardizes column names and concatenates them.
- Produces a single consolidated dataset: df_processed_final.csv.

3. `df_processed_final.csv`

- The final cleaned dataset, with the following columns:
- Tipo de Generación – Type of energy source
- Consumo(MW) – Maximum demand (MW)
- Mes – Month
- Año – Year

4. `eda.ipynb`

- Documents the data collection and cleaning process.
- Performs exploratory data analysis (EDA).
- Adds derived features such as seasons to analyze demand by time of year.
- Considers the following energy sources:
  - Aporte BESS
  - Eólica
  - Hidroeléctrica
  - Solar
  - Termoeléctrica

## 🔎 Key Insights
* Insight 1 – Main Sources of Energy Consumption
  - Hydroelectric and Thermoelectric are the dominant sources in Peru’s energy mix.
  - Therefore, the detailed analysis focuses on these two.

* Insight 2 – Yearly Extremes
  - Hydroelectric:
    - Maximum consumption: 2024 (47,984 MW)
    - Minimum consumption: 2018 (42,813 MW)

  - Thermoelectric:
    - Maximum consumption: 2024 (41,772 MW)
    - Minimum consumption: 2018 (28,779 MW)

➡️ Both sources reached their highest demand in 2024 and lowest in 2018.

* Insight 3 – Seasonal Patterns
  - Hydroelectric demand peaks in Autumn and Summer.
  - Thermoelectric demand peaks in Winter and Spring.
  - This seasonal variability reflects climatic influences on hydro resources and the balancing role of thermoelectric plants.

## 📌 Conclusion

- In recent years, thermoelectric generation has steadily increased, while hydroelectric production has remained stable.
- Solar and wind contributions remain low, despite potential for expansion.
- Key challenges for renewable integration include:
  - Seasonal variability (e.g., rainfall for hydro).
  - Legal and regulatory barriers delaying project execution.
  - Intermittency of wind and solar, which prevents them from ensuring a fully reliable supply.

- As a result, thermoelectric plants remain a crucial backup, despite their environmental cost.
- The record demand observed in 2024 reflects not only population/economic growth but also structural issues in Peru’s energy mix, highlighting the urgency of accelerating the energy transition.

## 🛠️ Installation / Dependencies
Ensure you have Python 3.8 installed. Then install required libraries:
```bash
pip install pandas beautifulsoup4 requests openpyxl matplotlib
```


▶️ Steps to Run

1. Run the web scraping script to download monthly reports:
```bash
python scrapping_coes.py
```

2. Run the preprocessing script to clean and consolidate the data:
```bash
python preprocess.py
```

3. Open and execute eda.ipynb to review the analysis and insights.

## 📌 Notes

- Data collection is limited to 2018–2024.
- Web scraping automates monthly updates, saving significant time compared to manual downloads.
- Preprocessing ensures consistency across reports with different formats.



