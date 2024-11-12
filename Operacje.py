


class Operation:
    def __call__(self, a, b):
        raise NotImplemented
    
    def name(self):
        return self.__class__.__name__

class Addition(Operation):
    def __call__(self, a, b):
        return a + b

class Multiply(Operation):
    def __call__(self, a, b):
        return a * b

class Division(Operation):
    def __call__(self, a, b):
        if b == 0:
            raise ValueError('cannot divide by 0')
        else:
            return a / b

class Subtraction(Operation):
    def __call__(self, a, b):
        return a - b


class Calculator():
    def __init__(self) -> None:
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)

    def calculate(self, x, y):
        for o in self.operations:
            print(f'Result of {o.name()}: {o(x, y)}')

calc = Calculator()
calc.add_operation(Addition())
calc.add_operation(Multiply())
calc.add_operation(Division())
calc.add_operation(Subtraction())
calc.calculate(10, 5)