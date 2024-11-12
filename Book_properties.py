class Book:
    def __init__(self, title, authnor, price, discount) -> None:
        self._title = title
        self._author = authnor
        self._price = price
        self._discount = discount

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def price(self):
        return self._price
    
    @property
    def discount(self):
        return self._discount
    
    @property
    def discount_price(self):
        return self.price - (self.price * self.discount)
    
    @title.setter
    def title(self, value):
        if value:
            self._title =  value
        else:
            raise ValueError('title cannot be empty string')
        
    @author.setter
    def author(self, value):
        if value:
            self._author = value
        else:
            raise ValueError('author cannot be empty string')
        
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError('price must be greater than 0')
        
    @discount.setter
    def discount(self, value):
        if value > 0:
            self._discount = value
        else:
            raise ValueError('discount must be greater than 0')
        
