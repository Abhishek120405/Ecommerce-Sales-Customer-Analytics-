# Setup Guide

## 1. Download and extract
Download the repository ZIP from GitHub (or clone it), then extract it.

## 2. Python environment (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python python/ecommerce_analysis.py
```

If PowerShell blocks activation, use Command Prompt:
```bat
.venv\Scripts\activate.bat
```

## 3. Interactive browser dashboard
Open `index.html` in Chrome or Edge. Use the dropdown filters and Reset Filters control. No server or external API is required.

## 4. Excel dashboard
Open `excel/Ecommerce_Sales_Analytics_Dashboard.xlsx` in Microsoft Excel Desktop. Start at the `Dashboard` worksheet. Change the six dropdowns to filter the dashboard; choose `All` to reset an individual filter. The workbook includes a `Read_Me` sheet.

## 5. SQLite SQL validation
```bash
python tests/run_sqlite_validation.py
```
This runs the SQLite-compatible companion query set against the included CSV.

## 6. PostgreSQL
Create/import a table named `sales_data` using `data/sales_data.csv`, then execute `sql/ecommerce_sales_analysis.sql` in PostgreSQL. The PostgreSQL script is supplied but is not represented as executed against a live server by this package.

## 7. Power BI Desktop
Import `data/sales_data.csv`, create measures from `power_bi/DAX_Measures.txt`, and follow `power_bi/Dashboard_Guide.md`. Save the resulting report as `Ecommerce_Sales_Customer_Analytics.pbix`. A native PBIX is not bundled because it must be authored and saved in Power BI Desktop.
