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