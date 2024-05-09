

# Python Test

Note: Formatting and type-annotations are a must!

1.  Define a bunch of variables holding values with the datatypes `int`, `str`, `float`, `complex`, `bool`, `NoneType`, `tuple[int]`, `list[str]`, `dict[str, int]`, and `set[tuple[float]]`.
1.  You ordered the following items from a restaurant. You must define a lambda that computes total price of all the items, a lambda that computes the tax, and a lambda that computes the total bill.  
      
    | Item     | Price  |
    | -        | -      |
    | Burger   | 139.99 |
    | Omelette | 79.99  |
    | Coke     | 99.99  |

    Tax is 18%

1.  Define a function `letter_frequency` that takes in an argument called `word` of type `str` and returns a mapping of each letter in word to its number of occurrences i.e. `dict[str, int]`.
1.  Define a bunch of classes `Restaurant`, `MenuItem`, `Customer`, `Cook`, `Waitress` with the following attributes.  
    1.  `Restaurant` has a `name`, `location` – a coordinate on x-y plane, `menu` – a bunch of menu-items, and `cooks`.  
    1.  `MenuItem` has a `name`, `price`, and `cooking_time` in seconds.  
    1.  `Customer` has a `name`, `location`, and `wishlist` – items he wants to eat.  
    1.  `Cook` has a `name`, `cooking_rate` – a speed boost which when multiplied with `cooking_time` gives the actual cooking time.  

    #### Restaurants
    1.  McDonald's situated at 5 km east and 10 km north of Town Center.  
        1. Menu  
            1.  Burger costs $14.99 and takes 3 minutes.
            1.  Coke costs $2.99 and takes 0.5 minutes.
            1.  Wrap costs $9.99 and takes 2 minutes.  
            1.  Omelette costs $7.99 and takes 3 minutes.  
        1. Cooks
            1.  Mac works at 1x speed
            1.  Francis works at 3x speed
    2.  BurgerKing situated at 7 km west and 10 km north of Town Center.  
        1. Menu  
            1.  Burger costs $12.99 and takes 5 minutes.
            1.  Coke costs $4.99 and takes 1 minutes.
            1.  Wrap costs $14.99 and takes 1 minutes.  
            1.  Omelette costs $3.99 and takes 5 minutes.  
        1. Cooks situated at 5 km east and 8 km south of Town Center.  
            1.  Alice works at 2x speed
            1.  Gene works at 1.5x speed
            1.  Penelope works at 1.25x speed
    3.  Dominos
        1. Menu  
            1.  Burger costs $12.99 and takes 5 minutes.
            1.  Coke costs $4.99 and takes 1 minutes.
            1.  Wrap costs $14.99 and takes 1 minutes.  
            1.  Omelette costs $3.99 and takes 5 minutes.  
            1.  Pizza costs $22.99 and takes 15 minutes
        1. Cooks
            1.  Bobby works at 1.75x speed
            1.  Diana works at 2.5x speed
            1.  Elliot works at 1x speed
    
    #### Customers
    1.  Zack situated at 4 km west and 3 km north of Town Center wants Pizza and Coke.
    1.  Yvetter situated at 2 km east and 9 km south of Town Center wants Wrap, Burger, and Omelette.
    1.  Xavier situated at 2 km south of Town Center wants Coke, Omelette, and Wrap
    1.  Wiona situated at 6 km east of Town Center wants Burger and Coke

    ### Questions
    1.  Find the nearest place each customer has to go so that he has wait the least.
    1.  Find the nearest place each customer has to go so that he has to spend the least.
    1.  How much money does a customer lose when he visits the least wait-time restaurant instead of least expensive restaurant.

    Note: One cook can cook only one dish at a time and has to cook it to the end.

1.  List all the builtins functions and use it in code samples. i.e. `print("Hi, there!")`.  
1.  Store the sentence – 'The quick brown fox jumps over the lazy dog' – in `base64` in a file and then read from, decode into `utf-8` and print on screen.
1.  Design a decorator, `add(n: int)`, such that it will always add `n` to any `int/float`-returning function.  
    For instance, design `add` such that the following code snippet does not fail  
    ```python
    add(3)
    def subtract(a: int, b: int):
        return a - b

    assert subtract(10, 6) == 7
    ```
1.  Design a class `Var` and use it as a context-manager so that the following snippet works.  
    ```python
    r = 20
    with Var(r) as x:
        x + 5
        x * 12
        x - 3
        x / 3
        x + 1
    
    assert x == 0
    ```
    Hint: User operator-overloading on a custom class inheriting from `int`.  
    Try the same snippet one more time with `r = 40` and find x.  
1.  Write the solution to each problem in a separate file `test_{i}.py` with the question number and put these files in a folder `quiz_1` and make it a package, so that each solution will be executed as `python -m quiz_1.test_{i}.py`.  
