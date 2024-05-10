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



