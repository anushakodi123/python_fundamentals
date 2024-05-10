# You ordered the following items from a restaurant. You must define a lambda that computes total price of all the items, a lambda that computes the tax, and a lambda that computes the total bill.

#     | Item     | Price  |
#     | -        | -      |
#     | Burger   | 139.99 |
#     | Omelette | 79.99  |
#     | Coke     | 99.99  |

#     Tax is 18%


burger = 13.99
omlette = 79.99
coke = 99.99
total_tax = 18

total_price = lambda burger, omlette, coke: burger + omlette + coke
tax = lambda total_price, tax: (total_price) * (tax / 100)
total_bill = lambda tax, total_price: tax + total_price

total_price = total_price(burger, omlette, coke)
tax = tax(total_price, total_tax)
total_bill = total_bill(tax, total_price)
print(total_price)
print(tax)
print(total_bill)