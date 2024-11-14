class MyMeta:
    def __new__(cls, name, bases, dct):
        # dodanie nowego atrybuty do klasy
        dct['class_id'] = 12345
        #zmodyfikowanie metody klasy
        orginal_method = dct.get('say_hello')
        if orginal_method:
            def new_method(self):
                print(f'Hello fromj {self.__class__.__name__}')
            dct['say_hello'] = new_method
        #tworzenie klasy
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass = MyMeta):
    def say_hello(self):
        print("hello")


obj = MyClass()
obj.say_hello()
print(obj.class_id)