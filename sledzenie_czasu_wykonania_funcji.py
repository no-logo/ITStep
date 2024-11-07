import time

def fun_wait():
    time.sleep(5)

def miernik_wykonania(f):
    licznik = 0
    def zmierz_czas():
        nonlocal licznik 
        licznik += 1
        t = time.time()
        f()
        return [time.time() - t, licznik]
    return zmierz_czas
        

miernik = miernik_wykonania()    

print(miernik())
    