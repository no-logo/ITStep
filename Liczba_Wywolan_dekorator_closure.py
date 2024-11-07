



from typing import Any


class FunctionCallTracker:
    def __init__(self, funkcja):
        self.funkcja = funkcja

    def __call__(self, *args, **kwargs):
        return self.funkcja(*args, **kwargs)

        

def fun_test():
    print('fun_test')


@FunctionCallTracker
def count_calls(fun, l):
    licznik = l
    def run_fun():
        nonlocal licznik
        licznik += 1
        fun()
        print(licznik)
    return run_fun

cc = count_calls(fun_test, 0)

cc()
cc(0)

