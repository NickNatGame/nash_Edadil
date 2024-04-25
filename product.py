class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_all_products(self):
        return self.name, self.price
