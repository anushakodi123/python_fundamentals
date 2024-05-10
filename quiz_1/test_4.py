from typing import Tuple
import math

class MenuItem:
    def __init__(self, name: str, price : float, cooking_time: int) -> None:
        self.name = name
        self.price = price
        self.cooking_time = cooking_time

class Cook:
    def __init__(self, name: str, cooking_rate: float) -> None:
        self.name = name
        self.cooking_rate = cooking_rate

class Customer:
    def __init__(self, name: str, location :Tuple[int, int], wishlist: list) -> None:
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
        distance_y = self.location[0] - customer.location[1]

        return math.sqrt(distance_x**2 + distance_y**2)

    def waiting_time(self, customer_wishlist):
        total_time = 0
        for item in customer_wishlist:
            for menu_item in self.menu:
                if item == menu_item.name:
                    time = menu_item.cooking_time
                    total_time += time
        return total_time
    
    def cook_speed(self):
        ...


menu_item1 = MenuItem("Burger", 14.99, 3)
menu_item2 = MenuItem("Coke", 2.99, 0.5)
menu_item3 = MenuItem("Wrap", 9.99, 2)
menu_item4 = MenuItem("Omelette", 7.99, 3)
cook1 = Cook("Mac", 1)
cook2 = Cook("Francis", 3)
restaurant1 = Restaurant("McDonald's", (5, 10), [menu_item1, menu_item2, menu_item3, menu_item4], [cook1, cook2])


menu_item5 = MenuItem("Burger", 12.99, 5)
menu_item6 = MenuItem("Coke", 4.99, 1)
menu_item7 = MenuItem("Wrap", 14.99, 1)
menu_item8 = MenuItem("Omelette", 3.99, 5)
cook3 = Cook("Alice", 2)
cook4 = Cook("Gene", 1.5)
cook5 = Cook("Gene", 1.25)
restaurant2 = Restaurant("BurgerKing", (-7, 10), [menu_item5, menu_item6, menu_item7, menu_item8], [cook3, cook4, cook5])

menu_item9 = MenuItem("Burger", 12.99, 5)
menu_item10 = MenuItem("Coke", 4.99, 1)
menu_item11 = MenuItem("Wrap", 14.99, 1)
menu_item12 = MenuItem("Omelette", 3.99, 5)
menu_item13 = MenuItem("Pizza", 3.99, 5)
cook6 = Cook("Bobby", 1.75)
cook7 = Cook("Diana", 2.5)
cook8 = Cook("Elliot", 1)
restaurant3 = Restaurant("Dominos", (5, -8), [menu_item9, menu_item10, menu_item11, menu_item12, menu_item13], [cook6, cook7, cook8])

customer1 = Customer("Zack", (-4, 3), ["Pizza", "Coke"])
customer2 = Customer("Yvetter", (2, -9), ["Wrap", "Burger", "Omletee"])
customer3 = Customer("Xavier", (0, -2), ["Coke", "Omlette", "Wrap"])
customer4 = Customer("Wiona", (6, 0), ["Burger", "Coke"])

restaurants = [restaurant1, restaurant2, restaurant3]
customers = [customer1, customer2, customer3, customer4]

for customer in customers:
    restaurants_distance = [{restaurant.name : restaurant.calculate_distance(customer)} for restaurant in restaurants]
    min_func = lambda d: min(d.values())
    min_dict = min(restaurants_distance, key = min_func)
    min_key = min(min_dict, key=min_dict.get)
    print(f"{customer.name} min distance restaurant:", min_key)

