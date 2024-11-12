class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Width must be positive')
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError('Height must be positive')
        
    @property
    def area(self):
        return self.width * self.height

rec = Rectangle(4,5)

print(rec.height, rec.width, rec.area)

rec.width = 40
rec.height = 50 

print(rec.height, rec.width, rec.area)