def dodaj_do(x):
    def dodaj(y):
        return x + y
    
    return dodaj

dodaj_50 = dodaj_do(50)

print(dodaj_50(10))
print(dodaj_50(40))
print(dodaj_do(50)(20))

def licznik():
    liczba = 0
    def zlicz():
        nonlocal liczba
        liczba += 1
        return liczba
    return zlicz

counter = licznik()

print(counter())
print(counter())
print(counter())
print(counter())

def filtruj_wieksze_od(limit):
    def filtruj(x):
        return x > limit
    return filtruj

wieksze_od_10 = filtruj_wieksze_od(10)

print(wieksze_od_10(20))
print(wieksze_od_10(5))