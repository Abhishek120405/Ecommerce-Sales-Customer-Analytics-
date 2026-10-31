# Excel Dashboard Update

- Added a single-screen `Dashboard` worksheet as the first sheet in the workbook.
- Added six dropdown filters: Region, Category, Sales Channel, Order Status, Month, and Day of Week.
- Added KPI cards for total orders, delivered revenue, estimated delivered profit, all-data unique customers, delivered orders, returned orders, cancelled orders, and average delivered order value.
- Added five Excel charts: daily delivered revenue trend, revenue by category, region, weekday, and top products.
- Dashboard visuals and formulas use the project's own `Sales_Data` worksheet (600 practice orders).
- Profit is an estimate from the supplied practice dataset; data is synthetic, not real company data.

## Validation scope

Workbook structure, six data validations, five embedded chart objects, formulas, and the 600-row source table were checked programmatically. Final recalculation/rendering should be confirmed in desktop Microsoft Excel because spreadsheet formula results depend on the spreadsheet engine.
