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

class Vehicle:
    def __init__(self, name, speed) -> None:
        self.name = name
        self.speed = speed

    def move(self):
        print('Vehicle is moving')

class Car(Vehicle):
    pass

c = Car('Car', 50)
c.move()

class Car2(Vehicle):
    def move(self):
        print('Drive')

c2 = Car2('Car', 50)
c2.move()

l = ['a', 'b', 'c', 'd']
it = iter(l)
print(next(it), next(it), next(it))

s = 'abscdlkan'
itr = iter(s)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

#klasy z możliwoscią iteracji

class MyIterable:
    def __iter__(self):
        self.a = 1
        return self    # wazne retukrn

    def __next__(self):
        x = self.a
        self.a += 3
        return x        # wazne retukrn
    
mi = MyIterable()
it = iter(mi)

print(next(it), next(it), next(it))

class MyRange:
    def __init__(self, start = 0, stop = 0, step = 1) -> None:
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        x = self.current
        
        if self.current >= self.stop:
            raise StopIteration
        self.current += self.step
        return x
    
r = MyRange(start = 0, stop = 10, step = 1)
it = iter(r)

for x in r:
    print(x)



it = iter(r)

for x in r:
    print(x)


#wyjatki

def get_num():
    user_input = input('Podaj numer: ')
    try:
        num = int(user_input)        
    except:
        print('Invalid input')
    else: 
        print('real number')
    finally:
        print('to się zawsze wykona tu można np zamykac plik')
    return num

        

#print(get_num())
#print(get_num())        
        
def write_to_file(path, text):
    file = open(path, 'a')

    try:
        file.write(text)
    except:
        print('faile to write into file')
    finally:
        file.close()

write_to_file(r"C:\users\User\ITStep\file.py",'\ntekst do zapisania w pliku\n')

def read_file(path):
    file = open(path, "r")

    try:
        print(file.read())
    except:
        print('error ocured')
    finally:
        file.close()

read_file(r"C:\users\User\ITStep\file.py")