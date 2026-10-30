# Setup Guide

## 1. Download and extract

Download the repository ZIP from GitHub or clone the repository, then extract it.

## 2. Interactive dashboard

Open `index.html` in Chrome or Edge. Use the Region, Category, Sales Channel, Order Status, Month and Day of Week filters and the Reset control. The dashboard runs locally without an external API.

## 3. Excel dashboard

Open `excel/Ecommerce_Sales_Analytics_Dashboard.xlsx` in Microsoft Excel Desktop and select the `Dashboard` sheet. It contains four dropdown filters and six charts. Supporting worksheets are `Insights`, `Sales_Data`, `Calc` and `About`.

## 4. Python analysis

```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install --upgrade pip
pip install -r requirements.txt
python python/ecommerce_analysis.py
```

## 5. SQLite validation

```bash
python tests/run_sqlite_validation.py
```

## 6. PostgreSQL

Import `data/sales_data.csv` into a table named `sales_data`, then execute `sql/ecommerce_sales_analysis.sql` in PostgreSQL. The SQL file is provided; live PostgreSQL execution is not claimed by this package.

## 7. Power BI Desktop

Import `data/sales_data.csv`, create measures from `power_bi/DAX_Measures.txt`, and follow `power_bi/Dashboard_Guide.md`. Save the report as a `.pbix` from Power BI Desktop. A native PBIX is not bundled.
