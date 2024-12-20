class ConstuctorMeta(type):
    def __new__(cls, name, bases, dct):
        attributes = dct.get('__atributes__', {})

        def __init__(self, **kwargs):
            for attr_name, attr_type in attributes.items():
                if attr_name in kwargs:
                    value = kwargs[attr_name]
                    if attr_type and not isinstance(value, attr_type):
                        raise TypeError('type error')
                    setattr(self, attr_name, value)
                else:
                    setattr(self, attr_name, None)
        


        dct['__init__'] = __init__

        return super().__new__(cls, name, bases, dct)
    
class ConstructorClass(metaclass = ConstuctorMeta):
    pass
    
class Person(ConstructorClass):
    __atributes__ = {"name" : str, "age"  : int}

p1 = Person(name = 'Alice', age = 30)
print(p1.name, p1.age)

p2 = Person(name = 'Alice2')
print(p2.name, p2.age)
