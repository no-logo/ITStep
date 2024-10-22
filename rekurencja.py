#funkcja rekurencyjna silnia n dla n > 0

def silnia(n):
    if n>1:
        return n * silnia(n-1)
    else:
        return 1
    
s = silnia(0)
print(s)

l1 = [1,2,3,10,20,30]
l2 = [4,5,6,40,50,60]
l3 = list(zip(l1,l2))
print(l3)

l4 = list(map(lambda x: x[0] + x[1], l3))
print(l4)

l5 = list(filter(lambda x: x > 10,l4))
print(l5)

import functools
l6 = functools.reduce(lambda a, b: a + b, l5)

print(l6)