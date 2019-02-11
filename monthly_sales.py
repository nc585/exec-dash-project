# monthly_sales.py

# TODO: import some modules and/or packages here

import os
import csv

csv_file_path = "sales-201803.csv" # a relative file path

rows = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for d in reader:
        rows.append(dict(d))

sales_prices = [float(row["sales price"]) for row in rows]
total_sales = sum(sales_prices)

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