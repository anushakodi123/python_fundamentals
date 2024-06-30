from functools import cache, cached_property, lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))
print(fibonacci.cache_info())

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))
print(fibonacci.cache_info())


class Customer:
    def __init__(self, orders) -> None:
        self.orders = orders

    @cached_property
    def recent_orders(self):
        orders = sorted(self.orders, key = lambda x: x["order_id"], reverse= True)
        return orders[:3]
    
orders = [
        {"order_id": 1, "name": "jgdhgs boots", "amount": 150, "qty": 1},
        {"order_id": 1, "name": "jgdhgs boots", "amount": 150, "qty": 1},
        {"order_id": 1, "name": "jgdhgs boots", "amount": 150, "qty": 1},
        {"order_id": 1, "name": "jgdhgs boots", "amount": 150, "qty": 1},
        {"order_id": 1, "name": "jgdhgs boots", "amount": 150, "qty": 1},
        {"order_id": 1, "name": "jgdhgs boots", "amount": 150, "qty": 1},
        {"order_id": 1, "name": "jgdhgs boots", "amount": 150, "qty": 1}

    ]

c = Customer(orders)

print(c.recent_orders)
print(c.recent_orders)