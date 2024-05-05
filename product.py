class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_json(self):
        return {"name": self.name, "price": self.price}