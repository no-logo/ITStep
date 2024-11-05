def stworz_rabat(rabat):
    def cena_po_rabacie(cena):
        return cena - (cena * rabat / 100)
    return cena_po_rabacie

black_friday_rabat = stworz_rabat(20)
cybar_monday_rabat = stworz_rabat(15)

print(black_friday_rabat(100))
print(cybar_monday_rabat(200))
print(black_friday_rabat(50))



