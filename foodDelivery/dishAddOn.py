class DishAddOn:
    def __init__(self, name, qty, price) -> None:
        self.name = name
        self.qty = qty
        self.price = price

    def get_price(self):
        return self.qty * self.price
    
