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

class Cube:
    a = 0
    def __init__(self, a) -> None:
        self.a = a
    def volume(self):
        return self.a ** 3
    
class Calculator:
    def __init__(self) -> None:
        self.history = []

    def add_to_history(self, operation, result):
        self.history.append((operation, result))
        return result

    def add(self, a, b):
        result = a + b
        return self.add_to_history(f'add {a} {b}', a + b)        
    
    def substract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    
calc = Calculator()
print(calc.add(3, 6))
print(calc.history)


class Person1:
    def __init__(self, fname, lname) -> None:
        self.first_name = fname
        self.last_name = lname

    def __str__(self) -> str:
        return f'Imię: {self.first_name} Nazwisko: {self.last_name}'

p = Person1('Jan', 'Nowak')
print(p)
    
class Student(Person1):
    def __init__(self, fname, lname, school) -> None:
        super().__init__(fname, lname)
        self.school = school

    def __str__(self) -> str:
        return super().__str__() + f' school: {self.school}'

s = Student('Piotr','Kowalski','II LO')
print(s)