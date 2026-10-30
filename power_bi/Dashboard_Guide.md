# Power BI Dashboard Build Guide

1. Open Power BI Desktop → Get Data → Text/CSV → select `data/sales_data.csv` → Load.
2. In Modeling → New measure, create the measures in `DAX_Measures.txt` one by one.
3. Add KPI cards: Total Orders, Delivered Orders, Delivered Revenue, Estimated Delivered Profit, Unique Customers, Average Delivered Order Value.
4. Add visuals:
   - Line chart: Order_Date (Month) vs Delivered Revenue
   - Clustered bar: Region vs Delivered Revenue
   - Bar chart: Product vs Delivered Revenue (Top N = 10)
   - Donut: Order_Status and Total Orders
   - Column chart: Category vs Delivered Revenue
5. Add slicers: Region, Category, Sales_Channel, Order_Date.
6. Format currency as INR, add titles, verify slicers, save as `Ecommerce_Sales_Customer_Analytics.pbix`.

The repository supplies prepared data, DAX measures, and layout instructions. It does not contain a native PBIX file.
