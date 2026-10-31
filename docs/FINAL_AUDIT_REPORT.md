# Final Project Audit Report

## Scope
Checks were run against the files in this repository package. This report does not claim that every external application or browser environment has been tested.

## Passed checks
- CSV contains 600 rows and 600 unique order IDs; statuses reconcile to 387 Delivered, 99 Returned and 114 Cancelled.
- Interactive HTML dashboard embeds valid JSON for all 600 rows and includes six filters, a reset control, chart canvases and a detail table.
- Dashboard copies are synchronized.
- Python analysis script executes and regenerates analysis outputs.
- Excel workbook includes 13 worksheets, five charts on the main Dashboard sheet, two charts on the Charts sheet and six dropdown validations.
- Notebook JSON is valid.
- All 10 SQLite companion queries execute against the included dataset and the row-count reconciliation passes.
- Eight ordered project image assets, including the Excel dashboard preview and interactive dashboard preview, are present in `images/`.
- README image references and ZIP archive integrity are checked during packaging.

## Not included / not claimed complete
- PostgreSQL SQL file is supplied but has not been executed against a live PostgreSQL server.
- A native Power BI `.pbix` is not included. DAX measures and a build guide are supplied; create and save the report in Power BI Desktop.
- GitHub repository upload/commit is not performed by this ZIP-generation process.
- GitHub Pages publication is not enabled automatically; configure it in repository Settings if you want a hosted dashboard page.
- Browser interactions and final appearance should still be checked in your own Chrome/Edge and Excel Desktop versions.
- The dataset is synthetic practice data for 2025; profit is estimated using assumed margins.

## Reproduce checks

```bash
python tests/validate_project.py
python tests/run_sqlite_validation.py
```
