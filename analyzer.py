import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    df["Revenue"] = df["Quantity"] * df["Price"]

    return df

def calculate_metrics(df: pd.DataFrame) -> dict:

    sales_by_product = df.groupby("Product")["Quantity"].sum()

    revenue_by_product = df.groupby("Product")["Revenue"].sum()

    return {
        "total_revenue": df["Revenue"].sum(),
        "total_quantity": df["Quantity"].sum(),
        "total_sales": len(df),
        "average_price": df["Price"].mean(),
        "best_seller": sales_by_product.idxmax(),
        "highest_revenue": revenue_by_product.idxmax(),
        "top5": revenue_by_product.sort_values(
            ascending = False
        ).head(5)
    }