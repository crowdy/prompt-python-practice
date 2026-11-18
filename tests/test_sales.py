from sales import month_of, monthly_totals, sales_of, best_month


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


def test_best_month_returns_month_with_highest_total():
    assert best_month({"2026-01": 520, "2026-02": 900, "2026-03": 320}) == "2026-02"


def test_best_month_ignores_empty_totals():
    assert best_month({}) == ""
