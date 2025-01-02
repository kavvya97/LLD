from dish import Dish
from typing import List
class Menu:
    def __init__(self, dishes: List[Dish]) -> None:
        self.dishes = dishes

    def get_dishes(self):
        return self.dishes