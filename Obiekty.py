class Person:
    name = 'Tom'
    age = 21

print(Person.name)
print(Person.age)

p = Person()
print(p.name, p.age)

p.age = 18
p.name = "Magda"
print(p.name, p.age)

class Person2:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'imie: {self.name}, wiek: {self.age}'
    
    def hello(self):
        print(f'Hello my name is {self.name}. I am {self.age} years old.')

p2 = Person2(name='Piotr', age=44)
print(p2.name, p2.age)

print(p2)

p2.hello()

class Circle:
    def __init__(self, r) -> None:
        self.radius = r

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def field(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.perimeter(), c.field()) 
    