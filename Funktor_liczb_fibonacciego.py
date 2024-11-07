
from typing import Any


class FibonacciGenerator:
    def __init__(self,start1,start2):
        self.start1 = start1
        self.start2 = start2
        self.fibo = []

    def __call__(self, *args, **kwds):
        if len(self.fibo) == 0:
            self.fibo.append(0)
        elif len(self.fibo) == 1:
            self.fibo.append(1)
        elif len(self.fibo) > 1:
            self.fibo.append(self.fibo[-1] + self.fibo[-2])

        return self.fibo[-1]

fibo_elem = FibonacciGenerator(0,1)

for i in range(10):
    print(f'element {i} = {fibo_elem()}')