# Final Project Audit Report

## Scope
This report records checks run against the files in this repository package. It does not claim that untested external applications or every possible browser environment are error-free.

## Passed checks
- CSV: 600 rows; 600 unique order IDs; status counts reconcile to 387 Delivered, 99 Returned, and 114 Cancelled.
- Interactive dashboard: embedded JSON parses; 600 embedded records match the CSV; required six filters, reset control, seven chart canvases, and table are present; root dashboard, `index.html`, and `outputs/Interactive_Dashboard.html` copies are checked for consistency by the included validation script.
- JavaScript: dashboard script passes Node.js syntax check.
- Python: analysis script runs and regenerates the included analysis outputs.
- Excel: workbook opens with 12 expected sheets, 601 rows including header on Sales_Data, and two embedded charts on the Charts sheet.
- Notebook: valid notebook JSON with 11 cells; prior package QA records a fresh-kernel execution.
- SQLite: all 10 companion analysis queries execute against the included dataset.
- Visuals: six PNG preview images are generated from this project's own synthetic sales dataset; they are not stock or unrelated illustrative images.
- README: all six embedded screenshot paths resolve.
- Archive: ZIP CRC/integrity test passes.

## Not verified / limitations
- PostgreSQL SQL file has not been executed against a live PostgreSQL server. The SQLite companion is tested separately.
- No native Power BI `.pbix` is included. DAX measures, CSV source, and build instructions are provided; create and validate the report in Power BI Desktop.
- Browser interaction has structural and JavaScript syntax checks, but the final visual/interaction check must be done in the user's Windows Chrome/Edge. Test every dropdown and Reset Filters.
- Excel formula recalculation and final visual appearance must be checked in desktop Microsoft Excel.
- GitHub Pages must be enabled in repository Settings; inclusion of `index.html` does not publish the site automatically.
- The 600-order dataset is synthetic practice data for 2025. `Profit_INR` is estimated from assumed margins, not audited business profit.

## Reproduce checks
From the repository root:

```bash
python tests/validate_project.py
python tests/run_sqlite_validation.py
node --check /path/to/extracted/dashboard.js
```

The dashboard JavaScript can be extracted from the `<script>` element in `Interactive_Dashboard.html` before running the Node syntax check.
