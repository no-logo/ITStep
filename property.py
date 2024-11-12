property(fget = None, fset = None, fdel = None, doc = None)

class Example():
    def __init__(self, value) -> None:
        self._value = value

    def get_value(self):
        return f'to jest wartosc: {self._value}'
    
    def set_value(self, value):
        if value >= 0:
            self._value = value
        else:
            raise ValueError('Value must be non-negative')
        
    value = property(get_value, set_value)

e = Example(10)

e.value = 5
print(e.value)
#e.value = -10 raise error