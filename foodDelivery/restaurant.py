from menu import Menu
from location import Location
class Restaurant:
    def __init__(self, restaurant_id, location: Location, menu: Menu, isAvail) -> None:
        self.restaurant_id = restaurant_id
        self.location = location
        self.menu = menu
        self.isAvail =  isAvail

    def add_menu(self,menu: Menu):
        self.menu = menu

    def prepare_food():
        print("Restaurant accepting the order and starting to prepare it")