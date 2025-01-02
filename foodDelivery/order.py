from dish import Dish
from user import User
from restaurant import Restaurant
from typing import List
class Order:
    order_id = 1
    def __init__(self, user: User, restaurant: Restaurant, dishes: List[Dish], discount_code=None) -> None:
        self.order_id = Order.order_id
        self.user = user
        self.restaurant = restaurant
        self.dishes = dishes
        self.orderStatus = "ACTIVE"
        self.discount_code = discount_code
        self.payment_status = "UNPAID"
        Order.order_id+=1

    def get_order_id(self):
        return self.order_id
    
    def get_dishes(self):
        return self.dishes
    
    def get_restaurant_id(self):
        return self.restaurant.get_id()


    
