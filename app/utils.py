
# utility function to convert float or integer "my_price" param to a usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71