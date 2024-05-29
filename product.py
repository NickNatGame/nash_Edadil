class Products:
    def __init__(self, name, price,image,store):
        self.name = name
        self.price = price
        self.image = image
        self.store = store

    def to_json(self):
        return {"name": self.name, "price": self.price, "image": self.image, "store": self.store}