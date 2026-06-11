def print_report(metrics: dict):

    print("=" * 40)
    print("         SALES REPORT")
    print("=" * 40)

    print(f"Total Revenue:      R$ {metrics['total_revenue']:.2f}")
    print(f"Units Sold:         {metrics['total_quantity']}")
    print(f"Total Sales:        {metrics['total_sales']}")
    print(f"Average Price:      R$ {metrics['average_price']:.2f}")

    print()

    print(f"Best Seller:        {metrics['best_seller']}")
    print(f"Highest Revenue:    {metrics['highest_revenue']}")

    print()

    print("Top 5 Products:")

    print(metrics["top5"])

    print("=" * 40)
