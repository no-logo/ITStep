class Person:
    def __init__(self,name, age) -> None:
        self._name = name
        self._age = age

    @property
    def age(self):
        """The age of the person"""
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("age > 0")
        else:
            self._age = value

    @age.deleter
    def age(self):
        print("deleting age")
        del self._age
        

person = Person('alice', 30)

print(Person.age.__doc__)

del person.age
#print(person.age)