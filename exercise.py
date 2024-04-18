print("Hello world")
print(1, 5.7, 3 / 3, 0xFF, 0b101, 0o777)


def bill(pizza_price: float, tax_rate: float = 0.18) -> float:
    tax = pizza_price * tax_rate
    total = pizza_price + tax
    return total


print(bill(300))
print(bill(450, 0.05))

students = ["alice", "bob", "cindy"]
students.insert(4, "dave")

for student in students:
    print(f"Welcome {student}")

students = {"alice": "math", "bob": "science", "cindy": "social"}
for key, value in students.items():
    print(f"{key} took the subject {value}")


def is_palindrome(word: str) -> bool:
    for i in range(0, len(word)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True


print(is_palindrome("student"))
print(is_palindrome("acaca"))
print(is_palindrome("mom"))
print(is_palindrome(""))


class Citizen:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hi {self.name}")

    def can_vote(self) -> bool:
        return self.age >= 18


alice = Citizen("alice", 17)
alice.say_hi()
print(alice.can_vote())


class Country:
    def __init__(self, name: str, voter_age: int):
        self.name = name
        self.voter_age = voter_age

    def can_vote(self, citizen: Citizen) -> bool:
        return citizen.age >= self.voter_age

    def __repr__(self) -> str:
        return self.name


india = Country("india", 23)
italy = Country("italy", 21)
bob = Citizen("bob", 20)
print(india.can_vote(bob))
print(italy.can_vote(bob))

students = ("alice", "bob", "cindy")
print(id(students))
students += ("dave",)
print(students)
print(id(students))

print(sorted(students))
print(sorted(students, reverse=True))
print(sorted(students, key=len))
print(sorted(students, key=lambda student: len(student) % 2))

countries = [india, italy]
print(sorted(countries, key=lambda country: country.name))
print(sorted(countries, key=lambda country: country.voter_age))

word = input("check if palindrome ")
print(is_palindrome(word))


def pipe(x, *funcs):
    for func in funcs:
        x = func(x)
    return x


pipe(word, is_palindrome, print)

add_1 = lambda n: n + 1
pipe(0, add_1, add_1, print)
