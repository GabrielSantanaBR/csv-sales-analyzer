import pandas as pd

# Read CSV
df = pd.read_csv("sales.csv")

print(df.head())

print()

print(df.info())

print()

print(df.describe())