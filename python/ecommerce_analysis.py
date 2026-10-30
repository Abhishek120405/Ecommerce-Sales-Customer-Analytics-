"""
E-Commerce Sales & Customer Analytics
Run from any directory: python python/ecommerce_analysis.py
Dataset: synthetic practice data; profit is estimated using assumed margins.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order_Date"])
required = ["Order_ID","Order_Date","Customer_ID","Region","Product","Category",
            "Quantity","Unit_Price_INR","Discount_Rate","Revenue_INR","Profit_INR",
            "Sales_Channel","Payment_Method","Order_Status"]
missing_cols = [c for c in required if c not in df.columns]
if missing_cols:
    raise ValueError(f"Dataset is missing expected columns: {missing_cols}")

# Basic validation / cleaning
df = df.drop_duplicates().copy()
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
for col in ["Quantity","Unit_Price_INR","Discount_Rate","Revenue_INR","Profit_INR"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=["Order_ID","Order_Date","Revenue_INR","Order_Status"])
delivered = df[df["Order_Status"].str.lower().eq("delivered")].copy()

def save_table(frame, name):
    frame.to_csv(OUT / name, index=False)

kpis = {
    "Total Orders": int(df["Order_ID"].nunique()),
    "Delivered Orders": int(delivered["Order_ID"].nunique()),
    "Returned Orders": int(df.loc[df["Order_Status"].str.lower().eq("returned"),"Order_ID"].nunique()),
    "Cancelled Orders": int(df.loc[df["Order_Status"].str.lower().eq("cancelled"),"Order_ID"].nunique()),
    "Unique Customers": int(df["Customer_ID"].nunique()),
    "Delivered Revenue INR": round(delivered["Revenue_INR"].sum(),2),
    "Estimated Delivered Profit INR": round(delivered["Profit_INR"].sum(),2),
    "Average Delivered Order Value INR": round(delivered["Revenue_INR"].sum()/max(delivered["Order_ID"].nunique(),1),2),
}
pd.DataFrame([{"Metric":k,"Value":v} for k,v in kpis.items()]).to_csv(OUT/"kpi_summary.csv",index=False)

for col, filename in [
    ("Region","revenue_by_region.csv"),
    ("Category","revenue_by_category.csv"),
    ("Sales_Channel","revenue_by_channel.csv"),
    ("Product","revenue_by_product.csv"),
]:
    result = delivered.groupby(col, as_index=False).agg(
        Orders=("Order_ID","nunique"), Revenue_INR=("Revenue_INR","sum"),
        Estimated_Profit_INR=("Profit_INR","sum"), Units=("Quantity","sum")
    ).sort_values("Revenue_INR",ascending=False)
    save_table(result,filename)

customer = delivered.groupby("Customer_ID",as_index=False).agg(
    Orders=("Order_ID","nunique"), Revenue_INR=("Revenue_INR","sum"),
    Estimated_Profit_INR=("Profit_INR","sum")
).sort_values("Revenue_INR",ascending=False)
save_table(customer.head(20),"top_20_customers.csv")

monthly = delivered.assign(Month=delivered["Order_Date"].dt.to_period("M").astype(str)).groupby(
    "Month",as_index=False
).agg(Orders=("Order_ID","nunique"),Revenue_INR=("Revenue_INR","sum"),
     Estimated_Profit_INR=("Profit_INR","sum"))
save_table(monthly,"monthly_trend.csv")

status = df.groupby("Order_Status",as_index=False).agg(Orders=("Order_ID","nunique"))
status["Share_Pct"] = (status["Orders"]/max(df["Order_ID"].nunique(),1)*100).round(2)
save_table(status,"order_status.csv")

# Charts
plt.figure(figsize=(10,5))
plt.plot(monthly["Month"],monthly["Revenue_INR"],marker="o")
plt.title("Monthly Delivered Revenue")
plt.xlabel("Month"); plt.ylabel("Revenue (INR)"); plt.xticks(rotation=45); plt.tight_layout()
plt.savefig(OUT/"monthly_revenue_trend.png",dpi=160); plt.close()

region = pd.read_csv(OUT/"revenue_by_region.csv")
plt.figure(figsize=(8,5))
plt.bar(region["Region"],region["Revenue_INR"])
plt.title("Delivered Revenue by Region"); plt.xlabel("Region"); plt.ylabel("Revenue (INR)")
plt.tight_layout(); plt.savefig(OUT/"revenue_by_region.png",dpi=160); plt.close()

topprod = pd.read_csv(OUT/"revenue_by_product.csv").head(10).sort_values("Revenue_INR")
plt.figure(figsize=(9,6))
plt.barh(topprod["Product"],topprod["Revenue_INR"])
plt.title("Top 10 Products by Delivered Revenue"); plt.xlabel("Revenue (INR)")
plt.tight_layout(); plt.savefig(OUT/"top_10_products.png",dpi=160); plt.close()

# Automatically generated descriptive findings
best_region = region.iloc[0]
best_product = pd.read_csv(OUT/"revenue_by_product.csv").iloc[0]
best_channel = pd.read_csv(OUT/"revenue_by_channel.csv").iloc[0]
report = [
    "# E-Commerce Sales & Customer Analytics — Results",
    "",
    "Dataset: synthetic practice data; profit is estimated using assumed margins.",
    "",
    "## KPI summary",
]
report += [f"- **{k}:** {v:,}" if isinstance(v,(int,float)) else f"- **{k}:** {v}" for k,v in kpis.items()]
report += [
    "",
    "## Descriptive findings",
    f"- Highest delivered revenue region in this dataset: **{best_region['Region']}** (₹{best_region['Revenue_INR']:,.2f}).",
    f"- Highest delivered revenue product in this dataset: **{best_product['Product']}** (₹{best_product['Revenue_INR']:,.2f}).",
    f"- Highest delivered revenue channel in this dataset: **{best_channel['Sales_Channel']}** (₹{best_channel['Revenue_INR']:,.2f}).",
    "",
    "## Interpretation limits",
    "- These are descriptive results from generated practice data, not evidence about a real retailer.",
    "- Profit is estimated and should not be described as audited financial performance.",
    "- Validate assumptions and explain the analysis before presenting it in an interview.",
]
(OUT/"executive_analysis_report.md").write_text("\n".join(report),encoding="utf-8")
print("Analysis completed. Outputs saved to:", OUT)
