# Define a bunch of variables holding values with the datatypes `int`, `str`, `float`, `complex`, `bool`, `NoneType`, `tuple[int]`, `list[str]`, `dict[str, int]`, and `set[tuple[float]]`.

a = 1
b = "Welcome!!"
c = 22.7
d = 3 + 5j
e = True
f = None
g = (1, 2, 3, 4)
h = ["Alice", "Bob", "Cindy", "Dev"]
i = {"math": 75, "science": 60, "physics": 80, "chemistry": 65}
j = {(1.7, 2.4, 6.3, 8.2)}


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



#Define a function `letter_frequency` that takes in an argument called `word` of type `str` and returns a mapping of each letter in word to its number of occurrences i.e. `dict[str, int]`.

def letter_frequency(word: str) -> dict:
    word_count = {}
    word_set = set(word.lower())

    for i in word_set:
        print(i, word)
        word_count[i] = word.lower().count(i)
    return word_count

print(letter_frequency("Andrea"))
