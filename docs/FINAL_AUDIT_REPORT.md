# Project Package Audit

## Checks performed for this package

- Source CSV contains 600 synthetic practice orders with unique order IDs.
- Order statuses reconcile to 387 Delivered, 99 Returned and 114 Cancelled.
- Delivered revenue: ₹36,07,684.18.
- Estimated delivered profit: ₹4,21,495.53 (assumption-based, not audited).
- Excel workbook opens programmatically, contains the Dashboard, Insights, Sales_Data, Calc and About worksheets, 600 source rows, six native charts and four dropdown validations.
- Excel dashboard default cached KPIs were checked against the source dataset.
- Main dashboard preview is included as `dashboard.png`.
- Interactive HTML dashboard and its source copy are included.
- Python analysis, Jupyter notebook, SQL scripts, DAX measures, setup guide, data dictionary and report are included.
- ZIP archive integrity and project validation scripts are checked during packaging.

## Not claimed as completed

- PostgreSQL SQL was not executed against a live PostgreSQL server.
- A native Power BI `.pbix` is not included. DAX measures and a build guide are supplied for creating it in Power BI Desktop.
- GitHub upload and GitHub Pages configuration are not performed by packaging this ZIP.
- Mobile preview rendering is not guaranteed to match desktop Microsoft Excel. Check the workbook in desktop Excel before final presentation.

## Reproduce checks

```bash
python tests/validate_project.py
python tests/run_sqlite_validation.py
```

## Data limitations

The dataset is synthetic practice data, not real company or customer data. Profit is estimated using assumed product margins.
