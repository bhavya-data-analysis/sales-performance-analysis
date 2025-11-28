import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. CREATE OUTPUT FOLDERS

os.makedirs("../outputs", exist_ok=True)
os.makedirs("../outputs/tables", exist_ok=True)
os.makedirs("../outputs/plots", exist_ok=True)


# 2. LOAD DATA

data_path = "../data/sales_data.csv"
df = pd.read_csv(data_path, parse_dates=["date"])

print("Data loaded successfully:")
print(df.head())

# 3. MONTHLY REVENUE ANALYSIS

df['month'] = df['date'].dt.to_period('M').astype(str)

monthly_revenue = df.groupby('month')['total'].sum().reset_index()

monthly_revenue.to_csv("../outputs/tables/monthly_revenue.csv", index=False)

plt.figure(figsize=(8,5))
sns.lineplot(data=monthly_revenue, x="month", y="total", marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../outputs/plots/monthly_revenue.png")
plt.close()

# 4. TOP PRODUCTS

top_products = df.groupby("product")['total'].sum().reset_index().sort_values(
    "total", ascending=False
)

top_products.to_csv("../outputs/tables/top_products.csv", index=False)

plt.figure(figsize=(8,5))
sns.barplot(data=top_products, x="total", y="product")
plt.title("Top Products by Revenue")
plt.xlabel("Revenue ($)")
plt.tight_layout()
plt.savefig("../outputs/plots/top_products.png")
plt.close()

# 5. TOP CUSTOMERS

top_customers = df.groupby("customer_id")["total"].sum().reset_index().sort_values(
    "total", ascending=False
)

top_customers.to_csv("../outputs/tables/top_customers.csv", index=False)

plt.figure(figsize=(8,5))
sns.barplot(data=top_customers, x="total", y="customer_id")
plt.title("Top Customers by Total Spend")
plt.xlabel("Total Spend ($)")
plt.tight_layout()
plt.savefig("../outputs/plots/top_customers.png")
plt.close()

# 6. CATEGORY ANALYSIS

category_sales = df.groupby("category")['total'].sum().reset_index()

category_sales.to_csv("../outputs/tables/category_sales.csv", index=False)

plt.figure(figsize=(8,5))
sns.barplot(data=category_sales, x="total", y="category")
plt.title("Sales by Product Category")
plt.xlabel("Revenue ($)")
plt.tight_layout()
plt.savefig("../outputs/plots/category_sales.png")
plt.close()

# 7. CITY-WISE SALES

city_sales = df.groupby("city")['total'].sum().reset_index().sort_values("total", ascending=False)

city_sales.to_csv("../outputs/tables/city_sales.csv", index=False)

plt.figure(figsize=(8,5))
sns.barplot(data=city_sales, x="total", y="city")
plt.title("Sales by City")
plt.xlabel("Revenue ($)")
plt.tight_layout()
plt.savefig("../outputs/plots/city_sales.png")
plt.close()

# DONE

print("\nAnalysis complete!")
print("Tables saved to outputs/tables/")
print("Plots saved to outputs/plots/")

