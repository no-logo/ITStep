class Shape:

    @staticmethod
    def area():
        return 'undefined area'
    
    def __str__(self) -> str:
        return 'Shape'
    
class Colored:

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'Colored'
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def __str__(self):
        return 'Circle'
    
class ColoredCircle(Circle, Colored):
    
    def __init__(self, radius, color):
        Circle.__init__(self,radius)
        Colored.__init__(self, color)

    def __str__(self):
        return f'Colored Circle of color {self.color}, radius {self.radius}'
    
    def __add__(self, other):
        if isinstance(other, ColoredCircle):
            new_radius = self.radius + other.radius
            if self.color == other.color:
                new_color = self.color
            else:
                new_color = 'mixed'
            return ColoredCircle(new_radius, new_color)
        else:
            NotImplemented
    
    def __mul__(self, n):
        self.radius = round(self.radius * n, 2)

    def __eq__(self, other):
        if isinstance(other, ColoredCircle):
            return self.radius == other.radius and self.color == other.color
        else:
            NotImplemented
    
cc1 = ColoredCircle(10, 'red')
cc2 = ColoredCircle(10, 'red')
cc3 = ColoredCircle(10, 'green')
cc4 = ColoredCircle(5, 'red')
    
print(cc1)
print(cc2)
print(cc3)
print(cc4)

print(cc1 + cc3)

print(cc1 == cc2)
print(cc1 == cc3)
print(cc1 == cc4)

cc1 * 3
print(cc1)
print(cc2.area())
    



        
        