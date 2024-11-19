


class MetaClass(type):
    def __new__(cls, name, bases, dct):
        dct['_num_of_instances'] = 0
        dct['get_instance_count'] = classmethod(lambda cls: cls._num_of_instances)
        print(type(super().__new__(cls,name,bases,dct)))
        return super().__new__(cls,name,bases,dct) # zwraca instancje metaklasy
    
    def __call__(cls, *args, **kwargs):
        cls._num_of_instances +=1
        print(type(super().__call__(*args, **kwargs)))
        return super().__call__(*args, **kwargs) # zwraca instancje klasy

print('=============')

class MyClass(metaclass = MetaClass):
    pass

print('------------')

obj1 = MyClass()
print(MyClass.get_instance_count())
obj2 = MyClass()     
print(MyClass.get_instance_count())
obj3 = MyClass()  
print(MyClass.get_instance_count())

print(type(obj1))
print(obj2.__dict__)