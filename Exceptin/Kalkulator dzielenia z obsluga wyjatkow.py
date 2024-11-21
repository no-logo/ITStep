def kalkulator_dzielenia():
    try:
        a = float(input('Podaj liczbe a: '))
    except ValueError:
        print('Nieprawidłowa wartość argumentu a')

    try:
        b = float(input('Podaj liczbe b: '))
    except ValueError:
        print('Nieprawidłowa wartość argumentu b')

    try:
        print(a /b)
    except ZeroDivisionError:
        print('błąd dzielenie przez zero')
    finally:
        print('przetwarzanie zakoncone')

#kalkulator_dzielenia()

def konwersja_listy(lst):
    nlst = []
    try:
        if len(lst) ==0:
            raise ValueError
    except ValueError:
        print('pusta lista')

    try:
        for n in lst:
            nlst.append(int(n))
        return nlst
    except ValueError:
        print('ta wartosc nie jest liczba calkowita')


class OutOfStockError(Exception):
    pass

def sklep():
    dostepnosc_produktu = 10
    try:
        ip = int(input('Podaj ilosc produktow: '))
    except ValueError:
        print('Nieprawidłowa wartość')
        return None


    try:
        if ip < 0 :
            raise ValueError
        elif ip > dostepnosc_produktu:
            raise OutOfStockError
    except ValueError:
        print('Ilosc nie moze byc mniejsa od 0')
    except OutOfStockError:
        print('za mala ilosc w magazynie')
    finally:
        print('dziekujemy za zakupy')

sklep()
