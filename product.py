class Products:
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

    def to_json(self):
        return {"name": self.name, "price": self.price, "image": self.image}