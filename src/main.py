from analyzer import load_data, calculate_metrics
from report import print_report, export_report
from charts import create_charts

df = load_data("sales.csv")

metrics = calculate_metrics(df)

print_report(metrics)

export_report(df)

create_charts(df)