print('')

x = y = z = 'orange'
print(x)
print(y)
print(z)

print('')

fruits = ["apple", "banana", "chery"]
x, y, z = fruits
print(x)
print(y)
print(z)

print('')

fruits = ["apple", "banana", "chery"]
x, *z = fruits
print(x)
print(z)

print('')

d = {'a'  : 1, 'b' : 2, 'c' : 3}
a1, *a = d
print(a1)
print(a)

print(globals())
print(globals()[a1])

dict1 = {'a':1}
print(dict1)

dict1.setdefault('b',2)
print(dict1)
print(dict1.get('b'))       # rekomendowane uzywanie get
print(dict1.get('c'))       # jeśli nie ma klucza w słowiniku zwraca None
print(dict1.get('c',10))    # jeśli nie ma klucza zwróci wartość przekazaną w get
                            # rekomendowane urzywanie get

x = 10.9
print(int(x))

price = 59
txt = f'The price is {price:.2f} dollars' # formatowanie ilości liczb po przecinku :.3f
print(txt)

# https://www.w3schools.com/python/default.asp fajne testy wszystkiego z pythone

