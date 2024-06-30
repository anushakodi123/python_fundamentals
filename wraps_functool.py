from functools import wraps


def my_decorator(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print("before executing function")
        func(*args, **kwargs)
        print("after executing function")
    return wrapper



def say_hello(name):
    """say hello
    
    parameters:
    name(string)
    """
    print(f"hello, {name}")

say_hello("Mike")
print(say_hello.__name__)
print(say_hello.__doc__)