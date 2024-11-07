

# funktor

from typing import Any


class Mnoznik:
    def __init__(self, mnoznik):
        self.mnoznik = mnoznik

    def __call__(self, x):
        return x * self.mnoznik
    

mnoz_przez_5 = Mnoznik(5)

wynik = mnoz_przez_5(10) #bez wywołania metody klasy

print(wynik)

# dekorator jako funkcja

def moj_dekorator(funkcja):
    def opakowanie():
        print("Przed wywołaniem")
        funkcja()
        print('Po wywołaniu')

    return opakowanie

@moj_dekorator
def przykladowa_funkcja():
    print('W środku funkcji')

przykladowa_funkcja()

#dekorator jako klasa
print('\n')

class LicznikWywolan:
    def __init__(self, funkcja):
        self.funkcja = funkcja
        self.licznik = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.licznik += 1
        print(f'Wywołano {self.licznik} razy {self.x}')
        return self.funkcja(*args, **kwargs)


@LicznikWywolan
def przykladowa_funkcja1():
    print('Dzialanie funkcji')

przykladowa_funkcja1()
przykladowa_funkcja1()

# dekoratory vs closures

def moj_dekorator(funkcja):
    def opakowanie():
        print("Przed wywołaniem")
        funkcja()
        print('Po wywołaniu')

    return opakowanie

@moj_dekorator
def przykladowa_funkcja2():
    print('W środku funkcji')

przykladowa_funkcja2()
