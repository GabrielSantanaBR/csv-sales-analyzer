from analyzer import load_data, calculate_metrics
from report import print_report

df = load_data("sales.csv")

metrics = calculate_metrics(df)

print_report(metrics)