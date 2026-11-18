"""Add up sales by month from a CSV file.

The CSV file has the columns date, item, qty, unit_price.
Run it with: uv run sales.py data/sample.csv
"""

import csv
import sys


def read_rows(path):
    """Read the CSV file and return its rows as a list of dictionaries."""
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def month_of(date):
    """Return the month of a date: "2026-01-05" -> "2026-01"."""
    return date[:7]


def sales_of(row):
    """Return the sales of one row: quantity times unit price."""
    return int(row["qty"]) * int(row["unit_price"])


def monthly_totals(rows):
    """Return a dictionary of total sales for each month."""
    totals = {}
    for row in rows:
        month = month_of(row["date"])
        if month not in totals:
            totals[month] = 0
        totals[month] = totals[month] + sales_of(row)
    return totals


def best_month(totals):
    """Return the month with the highest total sales."""
    best = ""
    for month in totals:
        if best == "" or totals[month] < totals[best]:
            best = month
    return best


def main():
    rows = read_rows(sys.argv[1])
    totals = monthly_totals(rows)
    for month in sorted(totals):
        print(month, totals[month])
    print("Best month:", best_month(totals))


if __name__ == "__main__":
    main()
