"""
computeSales module.

Reads product catalog and sales JSON files,
computes total sales cost and exports results.
"""

# pylint: disable=invalid-name

import json
import sys
import time
from typing import Any, Dict, Iterable, Optional


RESULTS_FILE = "SalesResults.txt"


def load_json_file(file_path: str) -> Optional[Any]:
    """Load JSON data from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file_handle:
            return json.load(file_handle)
    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format -> {file_path}")
        return None


def build_price_lookup(
    product_list: Iterable[Dict[str, Any]],
) -> Dict[str, float]:
    """Create a dictionary for product prices."""
    price_lookup: Dict[str, float] = {}
    for product in product_list:
        try:
            price_lookup[product["title"]] = float(product["price"])
        except (KeyError, TypeError, ValueError):
            print(f"Warning: Invalid product record {product}")
    return price_lookup


def compute_total_sales(
    price_lookup: Dict[str, float],
    sales_records: Iterable[Dict[str, Any]],
) -> float:
    """Compute total sales cost."""
    total_cost = 0.0
    for sale in sales_records:
        try:
            product_name = sale["Product"]
            quantity = float(sale["Quantity"])

            if product_name in price_lookup:
                total_cost += price_lookup[product_name] * quantity
            else:
                print(
                    f"Warning: Product not found in catalog -> {product_name}"
                )

        except (KeyError, TypeError, ValueError):
            print(f"Warning: Invalid sale record {sale}")
    return total_cost


def save_results(total_cost: float, elapsed_time: float) -> None:
    """Save results to a file."""
    try:
        with open(RESULTS_FILE, "w", encoding="utf-8") as file_handle:
            file_handle.write(f"Total Sales Cost: {total_cost:.2f}\n")
            file_handle.write(f"Execution Time: {elapsed_time:.4f} seconds\n")
    except OSError:
        print("Error writing results file")


def main() -> None:
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
