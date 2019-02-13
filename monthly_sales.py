# monthly_sales.py

import operator
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py

def to_usd(my_price):
    return f"${my_price:,.2f}"

# adapted from shopping cart project

#def main():
while True:
    # notes from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md
    print(os.listdir("/Users/Nina/Documents/Python/exec-dash-project/data")) 
    
    #guidance from Hiep
    csv_file_name = input("Please input the file name from the directory above in the format of sales-YYYYMM.csv: ")
    csv_file_path = os.path.join("data/",csv_file_name)     
    if not os.path.isfile(csv_filepath):
        print("We could not find your file. Please enter the exact file name from the directory above.")
    else:
        break
# adapted from https://github.com/s2t2/exec-dash-starter-py/commit/525446a5850d211bb78dfe1cb3ffb42ea4b3c9ad#diff-2bc9303c4e0187b3363d76974cc2fc8c


csv_data = pd.read_csv(csv_file_path)
monthly_total = csv_data["sales price"].sum()

# adapted from: https://github.com/s2t2/exec-dash-starter-py/commit/f790f124895db77920e37655c91e1e5a7a424aaa#diff-2bc9303c4e0187b3363d76974cc2fc8c
product_names = csv_data["product"]
unique_product_names = product_names.unique()
unique_product_names = unique_product_names.tolist()

top_sellers = [] 
for product_name in unique_product_names:
    matching_rows = csv_data[csv_data["product"] == product_name]
    product_monthly_sales = matching_rows["sales price"].sum()
    top_sellers.append({"name": product_name, "monthly_sales": product_monthly_sales})

top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)

# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_explore.py

def month_lookup(month):
    year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
    return year_month[month]

month = month_lookup(csv_file_name[-6:-4]) #pull this from file data values
year = int(csv_file_name[6:10]) #pull this from file or data values

# products = csv_data["product"].unique()
# products.sort()
# sales_price = csv_data.groupby(csv_data["product"]).sum()
# sales_price_col = list("sales price")
# total_price_by_prod = pd.DataFrame({"products":products, "sales price":sales_price_col})
# total_price_by_prod = total_price_by_prod.sort_values(by=["sales price"],ascending=False)

# for i in range(3):
# 	print(str(i+1)+') '+str(total_price_by_prod.iloc[i][0])+' ' "${0:,.2f}".format(total_price_by_prod.iloc[i][1])
# 			)

# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print(f"MONTH: {month} {year}")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

rank = 1
for d in top_sellers:
    print("  " + str(rank)+ ") " + d["name"]+ ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

# adapted from: https://github.com/s2t2/exec-dash-starter-py/commit/a0adfbe1af1b867889fdece114226cbd57657872#diff-2bc9303c4e0187b3363d76974cc2fc8c

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

# adapted from: https://github.com/s2t2/exec-dash-starter-py/commit/01b261ca30ee4c64d93c2146a1659ae2c9d445a5
sorted_products.reverse()
sorted_sales.reverse()

fig, ax = plt.subplots() 
usd_formatter = ticker.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(usd_formatter)

plt.barh(sorted_products, sorted_sales)
plt.xlabel(f"Monthly Sales (USD)")
plt.ylabel("Products")

for bar_index, bar_size in enumerate(sorted_sales):
    w = bar_size + 3
    h = bar_index - .1
    bar_label = to_usd(bar_size)
    ax.text(w, h, bar_label)

plt.title(f"Top Selling Products {month} {year}")
plt.tight_layout()
plt.show()
