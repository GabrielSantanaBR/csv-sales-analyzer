from analyzer import load_data, calculate_metrics
from report import print_report, export_report
from charts import create_charts

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--report", action="store_true")
parser.add_argument("--export", action="store_true")
parser.add_argument("--charts", action="store_true")
parser.add_argument("--all", action="store_true")

args = parser.parse_args()

df = load_data("src/sales.csv")
metrics = calculate_metrics(df)

if args.report:
    print_report(metrics)

if args.export:
    export_report(df)

if args.charts:
    create_charts(df)

if args.all:
    print_report(metrics)
    export_report(df)
    create_charts(df)