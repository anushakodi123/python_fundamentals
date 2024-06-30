from functools import wraps
from typing import Any
def f1(func):
    def wrapper():
        print("started")
        func()
        print("ended")
    
    return wrapper


@f1
def f():
    print("Hello world")

# print(f1(f)())
    
# print(f())


#with arguments

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


def start_end_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper

# def add_5(x):
#     return x+5

# print(add_5(10))

# print(help(add_5))
# print(add_5.__name__)

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello("Alice")


def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

# greet('Alex')
    



#class decorators

class CountCalls:

    def __init__(self, func) -> None:
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs) -> Any:
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc()


@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()


#timer decorator, debug decorator, check decorator, register functions, cache return value, get info or update the state