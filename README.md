# E-Commerce Sales & Customer Analytics

End-to-end Data Analyst portfolio project using Excel, SQL, Python, Jupyter Notebook, and Power BI resources.

## Dataset and limitations
This repository uses **synthetic practice data (600 orders, 2025)**. It is not real company/customer data. `Profit_INR` is estimated using assumed margins, not audited profit.

## Tools demonstrated
- Excel: prepared KPI dashboard, charts, supporting analysis sheets.
- Python: pandas, NumPy, data validation, aggregation, exploratory analysis, Matplotlib charts.
- SQL: KPI queries, filtering, aggregation, CTE, subquery, window functions, data-quality checks.
- Power BI: prepared DAX measures and report build guide.
- Business analysis: regional, product, channel, monthly and customer analysis.

## Repository map
- `data/`: source CSV
- `excel/`: prepared Excel dashboard
- `python/`: runnable analysis script
- `sql/`: PostgreSQL-compatible SQL queries
- `notebooks/`: Jupyter notebook
- `power_bi/`: DAX and dashboard guide
- `outputs/`: pre-generated CSV summaries, charts and executive report
- `docs/`: data dictionary

## Run Python
From the repository root:
```bash
python -m pip install -r requirements.txt
python python/ecommerce_analysis.py
```
The analysis outputs are already included in `outputs/`; running the script regenerates them.

## Run SQL
Import `data/sales_data.csv` into PostgreSQL as `sales_data`, then execute `sql/ecommerce_sales_analysis.sql`. The file contains table definition guidance and 10 ready-made queries.

## Power BI
Import the CSV in Power BI Desktop, create measures from `power_bi/DAX_Measures.txt`, follow `power_bi/Dashboard_Guide.md`, then save the report as a `.pbix` file. A native PBIX is not included.

## Before publishing
Review the outputs and make sure you can explain the analysis. Do not present synthetic data or estimated profit as real company results.


## Included visual deliverables
- `excel/Ecommerce_Sales_Analytics_Dashboard.xlsx`: prepared Excel dashboard and analysis tabs.
- `outputs/Interactive_Dashboard.html`: standalone interactive browser dashboard.
- `outputs/*.png`: Python-generated charts.
- `docs/Dashboard_Report.pdf`: static dashboard report.

## Completion status
Python analysis has been executed to generate the included CSV summaries, charts, and report. SQL queries are prepared but must be executed in a PostgreSQL database. Power BI DAX and build instructions are included, but a native `.pbix` report must be saved from Power BI Desktop.
