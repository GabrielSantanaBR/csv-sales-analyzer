# CSV Sales Analyzer

A Python project for sales data analysis using **Pandas** and **Matplotlib**.

This application reads sales data from a CSV file, calculates business metrics, generates reports, exports data to Excel and CSV, and creates charts automatically.

---

## Features

* Read sales data from CSV files
* Calculate total revenue
* Calculate total units sold
* Calculate average product price
* Find the best-selling product
* Find the product with the highest revenue
* Generate Top 5 products ranking
* Export reports to CSV
* Export reports to Excel
* Generate charts automatically
* Basic data validation and cleaning

---

## Technologies

* Python 3
* Pandas
* Matplotlib
* OpenPyXL

---

## Project Structure

```text
csv-sales-analyzer/

├── src/
│   ├── main.py
│   ├── analyzer.py
│   ├── report.py
│   └── charts.py
│
├── sales.csv
├── requirements.txt
├── README.md
└── output/
    ├── sales_report.csv
    ├── sales_report.xlsx
    ├── revenue_by_product.png
    └── quantity_by_product.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/csv-sales-analyzer.git
```

Enter the project directory:

```bash
cd csv-sales-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the complete analysis:

```bash
python src/main.py --all
```

Generate only the report:

```bash
python src/main.py --report
```

Export Excel and CSV files:

```bash
python src/main.py --export
```

Generate charts:

```bash
python src/main.py --charts
```

---

## Generated Outputs

The application automatically creates:

* `sales_report.csv`
* `sales_report.xlsx`
* `revenue_by_product.png`
* `quantity_by_product.png`

inside the `output/` directory.

---

## Example Metrics

* Total Revenue
* Total Units Sold
* Total Sales
* Average Price
* Best Selling Product
* Highest Revenue Product
* Top 5 Products by Revenue

---

## Purpose

This project was developed to demonstrate practical skills in:

* Data Cleaning
* Data Analysis
* CSV Processing
* Excel Export
* Python Automation
* Data Visualization

It can be used as a portfolio project for freelance platforms and junior Data Analyst opportunities.

---

## Author

Developed by **Gabriel Santana** as part of a data analysis and Python automation portfolio.

This project demonstrates practical skills in:
- Data Cleaning
- Data Analysis
- CSV Processing
- Excel Automation
- Data Visualization with Matplotlib