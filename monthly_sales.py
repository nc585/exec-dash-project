# monthly_sales.py

# TODO: import some modules and/or packages here

import os
import csv
import itertools
from operator import itemgetter

csv_file_name = "sales-201803.csv" # a relative file path

# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py 

csv_file_path = os.path.join("data",csv_file_name)

rows = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for d in reader:
        rows.append(dict(d))

sales_prices = [float(row["sales price"]) for row in rows]
total_sales = sum(sales_prices) #format this into USD 

# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py 

product_sales = []
sorted_rows = sorted(rows, key=itemgetter("product"))
rows_by_product = itertools.groupby(sorted_rows, key=itemgetter("product"))

for product, product_rows in rows_by_product:
    monthly_sales = sum([float(row["sales price"])for row in product_rows])
    product_sales.append({"name": product, "monthly_sales": monthly_sales})

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly sales", reverse=True))
top_sellers = sorted_product_sales[0:3]

month = "MARCH" #pull this from file data values
year = 2018 #put this from file or data values

# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
#print("MONTH: March 2018")
#print("MONTH: ", month, year)

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
#print("TOTAL MONTHLY SALES: $12,000.71")
print("TOTAL MONTHLY SALES: ", total_sales)

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

# make the charts here 