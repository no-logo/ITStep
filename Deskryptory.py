class ReadOnlyDescriptor:
    def __init__(self) -> None:
        self._value = 0
        self.__doc__ = "to jest deskryptor tylko do odczytu"

    def __get__(self, instance, owner):
        print("odczytuje wartosc")
        return self._value
    
    def __set__(self, instance, value):
        print("ustawiam wartosc")
        self._value = value

    def __delete__(self, instance):
        print("usuwam wartosc")
        del self._value
    

class MyClass:
    read_only = ReadOnlyDescriptor()  
    # read only musi być polek klasy nie polem obiektu

obj = MyClass()

print(obj.read_only)

class MyClass2:
    read_only2 = ReadOnlyDescriptor()
    # read only musi być polek klasy nie polem obiektu

    def __init__(self, value) -> None:
       self.read_only2 = value


obj2 = MyClass2(6)
print(obj2.read_only2)
print(MyClass2.read_only2)