from typing import Tuple
import math

class MenuItem:
    def __init__(self, name: str, price: float, cooking_time: int) -> None:
        self.name = name
        self.price = price
        self.cooking_time = cooking_time

class Cook:
    def __init__(self, name: str, cooking_rate: float) -> None:
        self.name = name
        self.cooking_rate = cooking_rate

class Customer:
    def __init__(self, name: str, location: Tuple[int, int], wishlist: list[MenuItem]) -> None:
        self.name = name
        self.location = location
        self.wishlist = wishlist

class Restaurant:
    def __init__(self, name: str, location: Tuple[int, int], menu: list[MenuItem], cooks: list[Cook]) -> None:
        self.name = name
        self.menu = menu
        self.location = location
        self.cooks = cooks

    def calculate_distance(self, customer: Customer):
        distance_x = self.location[0] - customer.location[0]
        distance_y = self.location[1] - customer.location[1]
        return math.sqrt(distance_x**2 + distance_y**2)

    

    def calculate_wait_time(self, customer_wishlist):
        total_time = 0
        for customer_item in customer_wishlist:
            min_waiting_time = float('inf')
            for menu_item in self.menu:
                if customer_item.name == menu_item.name:
                    for cook in self.cooks:
                        cooking_time = menu_item.cooking_time / cook.cooking_rate
                        min_waiting_time = min(min_waiting_time, cooking_time)
            total_time += min_waiting_time
        return total_time

    def calculate_cost_difference(self, customer_wishlist):
        min_cost = float('inf')
        for customer_item in customer_wishlist:
            for menu_item in self.menu:
                if customer_item.name == menu_item.name:
                    min_cost = min(min_cost, menu_item.price)
        return min_cost

menu_item1 = MenuItem("Burger", 14.99, 3 * 60)
menu_item2 = MenuItem("Coke", 2.99, 0.5 * 60)
menu_item3 = MenuItem("Wrap", 9.99, 2 * 60)
menu_item4 = MenuItem("Omelette", 7.99, 3 * 60)
cook1 = Cook("Mac", 1)
cook2 = Cook("Francis", 3)
restaurant1 = Restaurant("McDonald's", (5, 10), [menu_item1, menu_item2, menu_item3, menu_item4], [cook1, cook2])

menu_item5 = MenuItem("Burger", 12.99, 5 * 60)
menu_item6 = MenuItem("Coke", 4.99, 1 * 60)
menu_item7 = MenuItem("Wrap", 14.99, 1 * 60)
menu_item8 = MenuItem("Omelette", 3.99, 5 * 60)
cook3 = Cook("Alice", 2)
cook4 = Cook("Gene", 1.5)
cook5 = Cook("Penelope", 1.25)
restaurant2 = Restaurant("BurgerKing", (-7, 10), [menu_item5, menu_item6, menu_item7, menu_item8], [cook3, cook4, cook5])

menu_item9 = MenuItem("Burger", 12.99, 5 * 60)
menu_item10 = MenuItem("Coke", 4.99, 1 * 60)
menu_item11 = MenuItem("Wrap", 14.99, 1 * 60)
menu_item12 = MenuItem("Omelette", 3.99, 5 * 60)
menu_item13 = MenuItem("Pizza", 22.99, 15 * 60)
cook6 = Cook("Bobby", 1.75)
cook7 = Cook("Diana", 2.5)
cook8 = Cook("Elliot", 1)
restaurant3 = Restaurant("Dominos", (5, -8), [menu_item9, menu_item10, menu_item11, menu_item12, menu_item13], [cook6, cook7, cook8])

customer1 = Customer("Zack", (-4, 3), [menu_item13, menu_item6])
customer2 = Customer("Yvetter", (2, -9), [menu_item7, menu_item5, menu_item8])
customer3 = Customer("Xavier", (0, -2), [menu_item6, menu_item12, menu_item11])
customer4 = Customer("Wiona", (6, 0), [menu_item1, menu_item2])

restaurants = [restaurant1, restaurant2, restaurant3]
customers = [customer1, customer2, customer3, customer4]



for customer in customers:
    nearest_restaurant = min([restaurant1, restaurant2, restaurant3], key=lambda x: x.calculate_distance(customer))
    print(f"{customer.name} should go to {nearest_restaurant.name} for the least distance.")

    nearest_restaurant_wait = min([restaurant1, restaurant2, restaurant3], key=lambda x: x.calculate_wait_time(customer.wishlist))
    print(f"{customer.name} should go to {nearest_restaurant_wait.name} for the least wait time.")

    least_expensive_item_cost = min(nearest_restaurant.menu, key=lambda x: x.price).price
    least_wait_time_item_cost = sum([item.price for item in nearest_restaurant_wait.menu if item.name in customer.wishlist])
    cost_difference = least_wait_time_item_cost - least_expensive_item_cost
    print(f"{customer.name} loses ${cost_difference} by visiting the least wait-time restaurant instead of the least expensive restaurant.\n")

