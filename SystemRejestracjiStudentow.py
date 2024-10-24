import os

rejestr_studentow = dict()


def dodaj_studenta():
    imie = input('Podaj imię: ')
    nazwisko = input('Podaj nazwisko: ')
    nr_indeksu = input('Podaj nr indeksu: ')

    if nr_indeksu not in rejestr_studentow.keys():
        rejestr_studentow[nr_indeksu] = (imie, nazwisko)
    else:
        print('Taki nr indeksu już istnieje')

def wyszukaj_studenta():
    nr_indeksu = input('Podaj nr indeksu: ')
    if nr_indeksu in rejestr_studentow.keys():
        print(f'{nr_indeksu} - {rejestr_studentow[nr_indeksu][0]} {rejestr_studentow[nr_indeksu][1]}')
    else:
        print('Nie ma takiego nr indeksu w rejestrze')

def lista_studentow():
    for k in rejestr_studentow.keys():
        print(f'{k} - {rejestr_studentow[k][0]} {rejestr_studentow[k][1]}')

def usun_studenta():
    nr_indeksu = input('Podaj nr indeksu: ')
    if nr_indeksu in rejestr_studentow.keys():
        imie = rejestr_studentow[nr_indeksu][0]
        nazwisko = rejestr_studentow[nr_indeksu][1]
        rejestr_studentow.pop(nr_indeksu)
        print(f'Student {imie} {nazwisko} został usunięty.')
    else:
        print('Nie ma takiego nr indeksu w rejestrze')


os.system('cls')

opcja = 0

while opcja != 5:
    print("""
1. Dodaj Studenta
2. Wyszukaj Studenta
3. Wyświetl wszystkich studentów
4. Usuń Studenta
5. Zakończ
""")
    opcja = int(input('Wybierz opcję: '))
    if opcja not in [1,2,3,4,5]:
        print('brak takiej opcji')
    if opcja == 1:
        dodaj_studenta()
    elif opcja == 2:
        wyszukaj_studenta()
    elif opcja == 3:
        lista_studentow()
    elif opcja == 4:
        usun_studenta()



