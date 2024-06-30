# Design a class Var and use it as a context-manager so that the following snippet works.

# r = 20
# with Var(r) as x:
#     x + 5
#     x * 12
#     x - 3
#     x / 3
#     x + 1

# assert x == 0
# Hint: User operator-overloading on a custom class inheriting from int.
# Try the same snippet one more time with r = 40 and find x.



class Var(int):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        ...

    def __add__(self, other):
        return Var(super().__add__(other))

    def __sub__(self, other):
        return Var(super().__sub__(other))

    def __mul__(self, other):
        return Var(super().__mul__(other))

    def __truediv__(self, other):
        return Var(super().__truediv__(other))

r = 40
with Var(r) as x:
    x += 5
    x *= 12
    x -= 3
    x /= 3
    x += 1

print(x)



