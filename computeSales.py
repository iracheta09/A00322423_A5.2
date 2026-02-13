"""
computeSales module.

Reads product catalog and sales JSON files,
computes total sales cost and exports results.
"""

import json
import sys
import time


def load_json_file(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format -> {file_path}")
        return None


def build_price_lookup(product_list):
    """Create a dictionary for product prices."""
    price_lookup = {}
    for product in product_list:
        try:
            price_lookup[product["title"]] = product["price"]
        except KeyError:
            print(f"Warning: Invalid product record {product}")
    return price_lookup


def compute_total_sales(price_lookup, sales_records):
    """Compute total sales cost."""
    total_cost = 0
    for sale in sales_records:
        try:
            product_name = sale["Product"]
            quantity = sale["Quantity"]

            if product_name in price_lookup:
                total_cost += price_lookup[product_name] * quantity
            else:
                print(
                    f"Warning: Product not found in catalog -> {product_name}"
                )

        except KeyError:
            print(f"Warning: Invalid sale record {sale}")
    return total_cost


def save_results(total_cost, elapsed_time):
    """Save results to a file."""
    try:
        with open("SalesResults.txt", "w", encoding="utf-8") as file:
            file.write(f"Total Sales Cost: {total_cost:.2f}\n")
            file.write(f"Execution Time: {elapsed_time:.4f} seconds\n")
    except IOError:
        print("Error writing results file")


def main():
    """Main program execution."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py <productList.json> <sales.json>")
        sys.exit(1)

    product_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    product_list = load_json_file(product_file)
    sales_records = load_json_file(sales_file)

    if product_list is None or sales_records is None:
        print("Error loading data files.")
        sys.exit(1)

    price_lookup = build_price_lookup(product_list)
    total_cost = compute_total_sales(price_lookup, sales_records)

    elapsed_time = time.time() - start_time

    print(f"Total Sales Cost: {total_cost:.2f}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")

    save_results(total_cost, elapsed_time)


if __name__ == "__main__":
    main()
