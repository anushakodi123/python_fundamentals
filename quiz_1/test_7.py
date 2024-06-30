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