"""Add up sales by month from a CSV file.

The CSV file has the columns date, item, qty, unit_price.
Run it with: uv run sales.py data/sample.csv
"""

import csv
import sys

REPORT_PATH = "../prompt-python-practice-monthly-report.csv"


def read_rows(path):
    """Read the CSV file and return its rows as a list of dictionaries."""
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def month_of(date):
    """Return the month of a date: "2026-01-05" -> "2026-01"."""
    return date[:7]


def sales_of(row):
    """Return the sales of one row: quantitiy times unit price."""
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


def report_lines(totals):
    """Return the lines of the monthly report, with a total line at the end."""
    lines = ["month,sales"]
    for month in sorted(totals):
        if totals[month] < 500:
            continue
        grand_total = 0
        lines.append(month + "," + str(totals[month]))
        grand_total = grand_total + totals[month]
    lines.append("total," + str(grand_total))
    return lines


def write_report(totals, path=REPORT_PATH):
    """Write the monthly report to a CSV file."""
    with open(path, "w", encoding="utf-8") as f:
        for line in report_lines(totals):
            f.write(line + "\n")


def main():
    rows = read_rows(sys.argv[1])
    totals = monthly_totals(rows)
    for month in sorted(totals):
        print(month, totals[month])
    print("Best month:", best_month(totals))
    write_report(totals)
    print("Report written to", REPORT_PATH)


if __name__ == "__main__":
    main()
