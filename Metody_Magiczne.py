#materials.itstep.org/content/04c162fd-9837-49e1-8980

class MyClass:
    def __init__(self, value,items) -> None:
        self.value = value
        self.items = items

    def __str__(self) -> str:
        return f'To jest nasz obiekt a jego wartość wynosi {self.value}'
    
    def __eq__(self, other) -> bool:
        if isinstance(other, MyClass):
            return self.value == other.value
        else:
            return NotImplemented
    
    def __ne__(self, other) -> bool:
        return self.value != other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value


obj1 = MyClass(10,[1,12,3])
obj2 = MyClass(10,[1,2,3,4])

print(obj1)

print(obj1 == 10)
print(obj1 != obj2)
print(obj1 < obj2)
print(obj1 <= obj2)
print(obj1[0])
obj1[0] = 99
print(obj1[0])