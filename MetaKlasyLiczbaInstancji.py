


class MetaClass(type):
    _num_of_instances = 0
    def __new__(cls, name, bases, dct):
        dct['_num_of_instances'] = 0
        dct['get_instance_count'] = classmethod(lambda self: self._num_of_instances)
        return super().__new__(cls,name,bases,dct)
    
    def __call__(cls, *args, **kwargs):
        cls._num_of_instances +=1
        return super().__call__(*args, **kwargs)


class MyClass(metaclass = MetaClass):
    pass

obj1 = MyClass()
obj2 = MyClass()     
obj3 = MyClass()  

print(MyClass.get_instance_count())