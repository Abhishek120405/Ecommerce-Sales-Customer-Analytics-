# QA checklist and known validation boundaries

## Passed in this package build
- CSV contains 600 rows and the expected columns; order IDs are unique.
- Order statuses reconcile: 387 Delivered, 99 Returned, 114 Cancelled.
- Interactive HTML contains all six filters, reset control, seven chart canvases, and embedded JSON data matching the CSV row count.
- Root and outputs dashboard copies match.
- Python analysis script executes and regenerates the output summaries/charts/report.
- Excel workbook opens with 12 expected sheets and 2 embedded charts; source-data row count matches the CSV.
- Notebook JSON is valid and all notebook cells execute in a fresh Python kernel.
- All 10 SQLite-compatible SQL queries execute against the included CSV loaded into an in-memory SQLite database.
- README image paths resolve; ZIP archive integrity is checked after packaging.

## Not claimed as passed
- PostgreSQL execution: requires a PostgreSQL server; the PostgreSQL script is included but was not executed against a live server in this environment.
- Power BI native report: no `.pbix` is included. CSV, DAX measures, and build instructions are provided; final creation and validation must be done in Power BI Desktop.
- Browser rendering on the user's Windows machine: perform a final Chrome/Edge check after extraction, including changing each filter and using Reset Filters.
- Excel formula recalculation in Microsoft Excel: workbook structure and chart presence were checked, but final display should be confirmed in desktop Excel.

## Dataset caveats
- The 600-order dataset is synthetic practice data, not real company/customer data.
- Profit is estimated using assumed margins, not audited financial performance.
