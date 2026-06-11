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