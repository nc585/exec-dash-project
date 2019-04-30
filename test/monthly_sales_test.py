import os
import pandas

from app.monthly_sales import top_selling_products

def test_top_selling_products():
    # it should return a list of ranks, names and sales totals, sorted by sales ascending with top sellers first:
    csv_filename = "sales-201803.csv"
    csv_filepath = os.path.join(os.path.dirname(__file__), "mock_data", csv_filename)
    csv_data = pandas.read_csv(csv_filepath)
    results = top_selling_products(csv_data)
    expected_result = [
        {'rank': 1, 'name': 'Button-Down Shirt', 'monthly_sales': 6960.3499999999985},
        {'rank': 2, 'name': 'Super Soft Hoodie', 'monthly_sales': 1875.0},
        {'rank': 3, 'name': 'Khaki Pants', 'monthly_sales': 1602.0},
        {'rank': 4, 'name': 'Vintage Logo Tee', 'monthly_sales': 941.0500000000001},
        {'rank': 5, 'name': 'Brown Boots', 'monthly_sales': 250.0},
        {'rank': 6, 'name': 'Sticker Pack', 'monthly_sales': 216.0},
        {'rank': 7, 'name': 'Baseball Cap', 'monthly_sales': 156.31}
    ]


    assert results == expected_result
    