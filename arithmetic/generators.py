from random import randrange

def squares(i):
    return [x ** 2 for x in range(i)]

def rand(n):
    return [randrange(0,10) for _ in range(n)]

