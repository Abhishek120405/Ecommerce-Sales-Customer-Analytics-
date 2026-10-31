# QA checklist and known validation boundaries

## Passed in this package build
- CSV contains 600 rows and the expected columns; order IDs are unique.
- Order statuses reconcile: 387 Delivered, 99 Returned and 114 Cancelled.
- Interactive HTML contains all six filters, reset control, seven chart canvases, and embedded JSON data matching the CSV row count.
- Root and outputs dashboard copies match.
- Python analysis script executes and regenerates the output summaries/charts/report.
- Excel workbook contains 13 worksheets, five charts on the main Dashboard sheet, two charts on the Charts sheet, and six dropdown validations.
- Excel source-data row count matches the CSV.
- Notebook JSON is valid.
- All 10 SQLite-compatible SQL queries execute against the included CSV loaded into an in-memory SQLite database.
- All eight ordered project image assets are present in `images/`; README image references resolve.
- Required reports, DAX guide, SQL scripts and documentation are present.

## Not claimed as passed
- PostgreSQL execution: requires a PostgreSQL server; the PostgreSQL script is included but was not executed against a live server.
- Power BI native report: no `.pbix` is included. CSV, DAX measures, and build instructions are provided; final creation and validation must be done in Power BI Desktop.
- Browser rendering on the user's Windows machine: perform a final Chrome/Edge check after extraction, including changing each filter and using Reset Filters.
- Excel formula recalculation and visual appearance should be confirmed in desktop Excel.
- GitHub upload/commit is not performed by this ZIP-generation process.

## Dataset caveats
- The 600-order dataset is synthetic practice data, not real company/customer data.
- Profit is estimated using assumed margins, not audited financial performance.
