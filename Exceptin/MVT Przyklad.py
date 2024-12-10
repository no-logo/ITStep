#tworzenie modelu

class ProductModel:
    def __init__(self):
        self.products = [{"name":"laptop", "Price":1500}, {"name":"smartphone", "Price":800}, {"name":"headset", "Price":200}]

    def get_all_products(self):
        return self.products
    