from sales import month_of, monthly_totals, report_lines, sales_of, write_report


def test_month_of():
    assert month_of("2026-01-05") == "2026-01"


def test_sales_of():
    row = {"date": "2026-01-05", "item": "apple", "qty": "3", "unit_price": "120"}
    assert sales_of(row) == 360


def test_monthly_totals_one_row_per_month():
    rows = [
        {"date": "2026-01-05", "item": "apple", "qty": "3", "unit_price": "120"},
        {"date": "2026-02-03", "item": "apple", "qty": "5", "unit_price": "120"},
    ]
    assert monthly_totals(rows) == {"2026-01": 360, "2026-02": 600}


def test_report_lines():
    assert report_lines({"2026-01": 520}) == ["month,sales", "2026-01,520", "total,520"]


def test_write_report(tmp_path):
    path = tmp_path / "report.csv"
    write_report({"2026-01": 520}, path)
    assert path.read_text(encoding="utf-8") == "month,sales\n2026-01,520\ntotal,520\n"
