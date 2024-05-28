class Products:
    def __init__(self, name, price,image,shop):
        self.name = name
        self.price = price
        self.image = image
        self.shop = shop

    def to_json(self):
        return {"name": self.name, "price": self.price, "image": self.image, "shop": self.shop}