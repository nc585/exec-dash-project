# monthly_sales.py

import os
import pandas
import matplotlib.pyplot as plt

# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py

def to_usd(my_price):
    return f"${my_price:,.2f}"

csv_file_name = "sales-201803.csv" # TODO: change from relative to allow user input

# adapted from https://github.com/s2t2/exec-dash-starter-py/commit/525446a5850d211bb78dfe1cb3ffb42ea4b3c9ad#diff-2bc9303c4e0187b3363d76974cc2fc8c

csv_file_path = os.path.join(os.path.dirname(__file__),"data",csv_file_name)
csv_data = pandas.read_csv(csv_file_path)

# rows = []

# with open(csv_file_path, "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for d in reader:
#         rows.append(dict(d))

monthly_total = csv_data["sales price"].sum()

top_sellers = [
    {"name": "Button-Down Shirt", "monthly_sales": 6960.34},
    {"name": "Super Soft Hoodie", "monthly_sales": 1875.0},
    {"name": "Khaki Pants", "monthly_sales": 1602.0},
    {"name": "Vintage Logo Tee", "monthly_sales": 941.05},
    {"name": "Brown Boots", "monthly_sales": 250.0},
    {"name": "Sticker Pack", "monthly_sales": 216.0},
    {"name": "Baseball Cap", "monthly_sales": 156.31}
] # TODO: get from CSV data instead

# sales_prices = [float(row["sales price"]) for row in rows]
# total_sales = sum(sales_prices) #format this into USD 

# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py 

# product_sales = []
# sorted_rows = sorted(rows, key=itemgetter("product"))
# rows_by_product = itertools.groupby(sorted_rows, key=itemgetter("product"))

# for product, product_rows in rows_by_product:
#     monthly_sales = sum([float(row["sales price"])for row in product_rows])
#     product_sales.append({"name": product, "monthly_sales": monthly_sales})

# sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
# top_sellers = sorted_product_sales[0:3]

month = "MARCH" #pull this from file data values
year = 2018 #pull this from file or data values

# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
#print("MONTH: March 2018")
print(f"MONTH: {month} {year}")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

# rank = 1
# for d in top_sellers:
#     print("  " + str(rank)+ ") " + d["name"]+ ": " + to_usd(d["monthly_sales"]))
#     rank = rank + 1

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

# adapted from: https://github.com/s2t2/exec-dash-starter-py/commit/a0adfbe1af1b867889fdece114226cbd57657872#diff-2bc9303c4e0187b3363d76974cc2fc8c

chart_title = "Top Selling Products (March 2018)" #TODO: get month and year

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

plt.bar(sorted_products, sorted_sales)
plt.ylabel("Monthly Sales (USD)")
plt.xlabel("Products")
plt.show()
