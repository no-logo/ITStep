from typing import Any


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'[Meta __new__] Tworzenie klasy {name}')
        cls = super().__new__(cls, name, bases, dct)
        print(f'[Meta __new__] kalsa {name} utworzona')
        return cls

    def __init__(cls, name , bases, dct):
        print(f'[Meta __init__] inicjalizacja klasy {name}')
        super().__init__(name, bases, dct)

    def __call__(cls, *args, **kwds):
        print(f'[Meta __call__] wywolanie klasy {cls.__name__} z argumentami {args}, {kwds}')
        instance =  super().__call__(*args, **kwds)
        print(f'[Meta __call__] wywolanie klasy {cls.__name__} z argumentami {args}, {kwds}')
        return instance
      
    
class MyClass(metaclass = MyMeta):

    def __new__(cls, value):
        print(f'[my class __new__] tworzenie instacji klasy my class')
        instance = super().__new__(cls)
        return instance

    def __init__(self, value) -> None:
        print(f'[Myclass __init__] tworzenie instancji klasy {value}')
        self.value = value


    def __call__(self, *args, **kwargs):
        print('[Myclass __call__]')
        return sum(args)
    
print('zaczynamy')
print('\n tworzenie klasy my class\n')
print('tworzenie instancji klasy myclass')
instance = MyClass(42)
print('wywolywanie instacni klasy my class')
result = instance(10, 20)
print(f'wynik wywołania instancji {result}')