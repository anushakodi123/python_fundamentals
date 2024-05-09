import base64

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


# Define a function `letter_frequency` that takes in an argument called `word` of type `str` and returns a mapping of each letter in word to its number of occurrences i.e. `dict[str, int]`.


def letter_frequency(word: str) -> dict:
    word_count = {}
    word_set = set(word.lower())

    for i in word_set:
        print(i, word)
        word_count[i] = word.lower().count(i)
    return word_count


print(letter_frequency("Andrea"))


# List all the builtins functions and use it in code samples. i.e. `print("Hi, there!")`.

a = [1, 2, 3, 4]
print(len(a))
print(type(a))
print(sum(a))
print(max(a))
print(min(a))
b = ("a", "b", "c")
c = (1, 2, 3, 4)
print(tuple(zip(b, c)))
print(list(c))

# Store the sentence – 'The quick brown fox jumps over the lazy dog' – in base64 in a file and then read from, decode into utf-8 and print on screen.
a = "The quick brown fox jumps over the lazy dog"
encoded_sentence = base64.b64encode(a.encode("utf-8"))

with open("encoded_sentence.txt", "wb") as file:
    file.write(encoded_sentence)

with open("encoded_sentence.txt", "rb") as file:
    encoded_sentence = file.read()

decoded_sentence = base64.b64decode(encoded_sentence).decode("utf-8")

print(decoded_sentence)


# Design a decorator, add(n: int), such that it will always add n to any int/float-returning function.
# For instance, design add such that the following code snippet does not fail

# add(3)
# def subtract(a: int, b: int):
#     return a - b

# assert subtract(10, 6) == 7


def add(a: int) -> int:
    def wrapper(func):
        def adding(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + a

        return adding

    return wrapper


@add(3)
def subtract(a: int, b: int) -> int:
    return a - b


print(subtract(10, 3))


