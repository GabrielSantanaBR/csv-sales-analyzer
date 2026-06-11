import pandas as pd

# Read CSV
df = pd.read_csv("sales.csv")

df["Revenue"] = df["Quantity"] * df["Price"]

total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()
total_sales = len(df)
average_price = df["Price"].mean()

print(f"Total Revenue: R$ {total_revenue:.2f}")
print(f"Total Units Sold: {total_quantity}")
print(f"Total Sales: {total_sales}")
print(f"Average Price: R$ {average_price:.2f}")

print()

sales_by_product = df.groupby("Product")["Quantity"].sum()
revenue_by_product = df.groupby("Product")["Revenue"].sum()
best_seller = sales_by_product.idxmax()
highest_revenue = revenue_by_product.idxmax()
top5 = revenue_by_product.sort_values(ascending=False).head(5)

print(sales_by_product)
print()
print(revenue_by_product)
print()
print(f"Best Selling Products: {best_seller}")
print()
print(f"Highest Revenue Product: {highest_revenue}")
print()
print(top5)