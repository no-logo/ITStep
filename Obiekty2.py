class A:
    a = 5

class B:
    b = 10

class C(A, B):
    c = 20

print(C.a, C.b, C.c)

class Car:
    def __init__(self, brand) -> None:
        self.brand = brand

    def move(self):
        print('Drive!')

class Boat:
    def __init__(self, brand) -> None:
        self.brand = brand

    def move(self):
        print('Sail!')

class Plane:
    def __init__(self, brand) -> None:
        self.brand = brand

    def move(self):
        print('Fly!')

car, boat, plane = Car('Cadilac'), Boat('Elan'), Plane('Cesna')

for x in (car, boat, plane):
    x.move()                    #POLIMORFIZM X WYOŁUJE JEDNĄ METODĘ I JEST WOŁANA ODPOWIEDNIA DLA KAŻDEJ KLASY
    
