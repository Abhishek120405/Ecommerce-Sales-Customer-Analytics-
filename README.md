# E-Commerce Sales & Customer Analytics

**End-to-end Data Analytics portfolio project** | Excel · SQL · Python · Interactive HTML · Jupyter · Power BI (DAX guide)

An end-to-end practice project analyzing 600 synthetic e-commerce orders from 2025. It explores sales performance across products, categories, regions, sales channels, customers, order status and time.

> **Data transparency:** The dataset is synthetic practice data, not real company or customer data. Profit is an estimate based on assumed product margins; it is not audited company profit. All findings are demonstrations of analytical methods, not claims about a real business.

## Dashboard preview

![E-Commerce Sales & Customer Analytics Dashboard](dashboard.png)

### Open the interactive dashboard

- Open [`index.html`](index.html) in Chrome or Edge. The browser dashboard includes filters, KPI cards, charts and a detail table; it runs locally without an external API.
- The same dashboard source is also available at [`Interactive_Dashboard.html`](Interactive_Dashboard.html).

### Excel dashboard

Open [`excel/Ecommerce_Sales_Analytics_Dashboard.xlsx`](excel/Ecommerce_Sales_Analytics_Dashboard.xlsx) in Microsoft Excel Desktop and select the **Dashboard** sheet.

The workbook contains:
- 4 dropdown filters: Region, Category, Sales Channel and Month
- 6 KPI cards: Total Orders, Delivered Revenue, Estimated Delivered Profit, Average Order Value, Return Rate and Cancellation Rate
- 6 native Excel charts: monthly delivered revenue, category revenue share, delivered revenue by region, orders by weekday, top 5 products and order-status split
- Supporting sheets: `Insights`, `Sales_Data`, `Calc` and `About`

The workbook's dashboard is designed for desktop Excel. Spreadsheet rendering can vary in mobile preview apps and other spreadsheet programs.

## Verified dataset summary

| Metric | Value |
|---|---:|
| Total orders | 600 |
| Delivered orders | 387 |
| Returned orders | 99 |
| Cancelled orders | 114 |
| Delivered revenue | ₹36,07,684.18 |
| Estimated delivered profit | ₹4,21,495.53 |
| Unique customers | 175 |
| Average delivered order value | ₹9,322.18 |

Delivered revenue and estimated profit include delivered orders only. Return and cancellation rates use all orders as the denominator.

## Project structure

```text
.
├── .github/workflows/       # Automated validation workflow
├── dashboard.png            # Main Excel dashboard preview for GitHub
├── data/sales_data.csv      # 600 synthetic practice orders
├── docs/                    # Setup, audit, data dictionary, QA and report docs
├── excel/                   # Final Excel dashboard workbook
├── notebooks/               # Jupyter analysis notebook
├── outputs/                 # KPI tables, analysis results and chart exports
├── power_bi/                # DAX measures and Power BI build guide
├── python/                  # Reproducible pandas analysis
├── sql/                     # PostgreSQL and SQLite query scripts
├── tests/                   # Project and SQL validation scripts
├── index.html               # Interactive dashboard entry point
├── Interactive_Dashboard.html
├── Dashboard_Report.pdf
├── requirements.txt
└── LICENSE
```

## Run the project

### Python analysis

```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install --upgrade pip
pip install -r requirements.txt
python python/ecommerce_analysis.py
```

### SQLite query validation

```bash
python tests/run_sqlite_validation.py
```

### PostgreSQL

Import `data/sales_data.csv` into a table named `sales_data`, then run [`sql/ecommerce_sales_analysis.sql`](sql/ecommerce_sales_analysis.sql) in PostgreSQL. The PostgreSQL script is included but has not been run against a live PostgreSQL server as part of this package build.

### Power BI Desktop

Import `data/sales_data.csv`, create the measures in [`power_bi/DAX_Measures.txt`](power_bi/DAX_Measures.txt), and follow [`power_bi/Dashboard_Guide.md`](power_bi/Dashboard_Guide.md). Save the finished report in Power BI Desktop. **A native `.pbix` file is not included.**

For detailed instructions, see [`docs/SETUP_GUIDE.md`](docs/SETUP_GUIDE.md).

## Validation

Run:

```bash
python tests/validate_project.py
python tests/run_sqlite_validation.py
```

The checks cover the CSV structure and row counts, HTML dashboard data, Excel workbook structure and charts, notebook JSON, required documentation and SQLite-compatible SQL queries. GitHub Actions runs these checks on pushes and pull requests.

**Validation boundaries:** PostgreSQL execution against a live server and creation of a native Power BI `.pbix` remain separate steps. Check the dashboard in your own desktop Excel and browser after downloading the repository.

## License

Project code and documentation are released under the MIT License. The synthetic dataset is included for practice and demonstration.
