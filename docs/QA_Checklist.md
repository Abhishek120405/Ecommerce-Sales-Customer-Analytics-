# QA Checklist

## Package checks

- [ ] `data/sales_data.csv` contains 600 rows and unique order IDs.
- [ ] Status totals reconcile: 387 Delivered, 99 Returned, 114 Cancelled.
- [ ] `dashboard.png` exists and displays the dashboard overview.
- [ ] `index.html` opens in Chrome or Edge and filters respond.
- [ ] Excel workbook contains five sheets, 600 data rows, six charts and four dropdown filters.
- [ ] `python tests/validate_project.py` passes.
- [ ] `python tests/run_sqlite_validation.py` passes.
- [ ] GitHub Actions workflow completes successfully after push.

## User-side checks

- [ ] Open the Excel workbook in desktop Microsoft Excel and inspect the Dashboard sheet.
- [ ] Change each dropdown filter and confirm the KPI/chart updates.
- [ ] Open the HTML dashboard and test each filter plus Reset.
- [ ] If creating a Power BI report, save and validate the `.pbix` separately.

## Known boundaries

- Dataset is synthetic practice data.
- Profit is estimated using assumed margins.
- PostgreSQL script is supplied but not verified against a live PostgreSQL server.
- A native Power BI `.pbix` is not included.
