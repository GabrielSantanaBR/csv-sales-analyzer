import os
import matplotlib.pyplot as plt
import pandas as pd

def create_charts(df: pd.DataFrame):

    os.makedirs("output", exist_ok=True)

    revenue = df.groupby("Product")["Revenue"].sum()

    plt.figure(figsize=(10,6))
    revenue.sort_values().plot(kind="barh")
    plt.title("Revenue by Product")
    plt.xlabel("Revenue (R$)")
    plt.tight_layout()
    plt.savefig("output/revenue_by_product.png")
    plt.close()

    quantity = df.groupby("Product")["Quantity"].sum()

    plt.figure(figsize=(10, 6))
    quantity.sort_values().plot(kind="barh")
    plt.title("Quantity Sold by Product")
    plt.xlabel("Units Sold")
    plt.tight_layout()
    plt.savefig("output/quantity_by_product.png")
    plt.close()