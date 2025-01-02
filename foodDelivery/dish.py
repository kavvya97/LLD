from dishAddOn import DishAddOn

class Dish:
    def __init__(self, name, cuisine, price):
        self.name = name
        self.cuisine = cuisine
        self.description = ""
        self.price = price
        self.dish_images = []
        self.addons = []

    def add_addon(self, addon):
        self.addons.append(addon)

    def remove_addon(self, addon):
        self.addons.remove(addon)

    def get_price(self):
        total_price = self.price
        for addon in self.addons:
            total_price += addon.get_price()
        return total_price

    def get_description(self):
        return self.description

    def get_dish_name(self):
        return self.name

    def get_cuisine(self):
        return self.cuisine
