from typing import Any


class CustomMeta(type):
    _instances = {}

    # __new__ jest wywoływane jak program napotka na definicje klasy MyClass
    def __new__(cls, name, bases, dct):
        # dodajemy mową metodę do każdej klasy tworzonej prze tę metaklasę
        dct['describe'] = lambda self: f'this is instance of {name} with attributes {self.__dict__}'
        print(f'creating class {name} with bases {bases} and attributes {list(dct.keys())}')
        print('====',type(super().__new__(cls, name, bases, dct)))
        return super().__new__(cls, name, bases, dct) 
    
    # __call__ jest wywoływana przy tworzeniu obiektu obj1 i obj1
    def __call__(cls, *args, **kwargs):
        # kontrolujemy proces tworzenia instancji (np singleton)
        if cls not in cls._instances:
            print('creating new instance')
            print('====',type(super().__call__(*args, **kwargs)))
            cls._instances[cls] = super().__call__(*args, **kwargs) #zwraca instancję obiektu
        else:
            print('reusing existing instance')
        
        return cls._instances[cls]
    
class MyClass(metaclass = CustomMeta):
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


obj1 = MyClass('first', 10)
print(obj1.describe())

obj2 = MyClass('second', 20)
print(obj2.describe())
        