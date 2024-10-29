

#MATERIALY
# https://materials.itstep.org/content/04c162fd-9837-49e1-8980-2fbceaf88bb8/pl

class Human():

    def __init__(self,first_name, last_name, date_of_birth, contact_number, city, country, address) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__contact_number = contact_number
        self.__city = city
        self.__coutry = country
        self.__address = address

    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_date_of_birth(self):
        return self.__date_of_birth
    def get_contact_number(self):
        return self.__contact_number
    def get_city(self):
        return self.__city
    def get_country(self):
        return self.__coutry
    def get_address(self):
        return self.__address
    
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth
    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number
    def set_city(self, city):
        self.__city = city
    def set_country(self, coutry):
        self.__coutry = coutry
    def set_address(self, address):
        self.__address = address

class City:
    def __init__(self, nazwa_miasta, nazwa_regionu, nazwa_kraju, liczba_mieszkancow, kod_pocztowy, nr_kierunkowy) -> None:
        self.__nazwa_miasta = nazwa_miasta
        self.__nazwa_regionu = nazwa_regionu
        self.__nazwa_kraju = nazwa_kraju
        self.__liczba_mieszkancow = liczba_mieszkancow
        self.__kod_pocztowy = kod_pocztowy
        self.__nr_kierunkowy = nr_kierunkowy

    @classmethod
    def create_class_from_input(cls):
        nazwa_miasta = input('Podaj nazwe miasta: ')
        nazwa_regionu = input('Podaj nazwe regionu: ')
        nazwa_kraju = input('Podaj nazwe kraju: ')
        liczba_mieszkancow = input('Podaj liczbe mieszkancow: ')
        kod_pocztowy = input('Podaj kod pocztowy: ')
        nr_kierunkowy = input('Podaj nr kierunkowy: ')
        return (cls(nazwa_miasta, nazwa_regionu, nazwa_kraju, liczba_mieszkancow, kod_pocztowy, nr_kierunkowy))
    
    def get_city_info(self):
        return self.__nazwa_miasta + ' ' + self.__nazwa_regionu + ' ' + self.__nazwa_kraju + ' ' + self.__liczba_mieszkancow


if __name__ == "__main__":

    human = Human('Andrzej', 'Wawryk', '1975-01-03', '536956536', 'Kraków', 'Polska', 'Ulica 1/23 12-345 Kraków')

    print(human.get_first_name())
    print(human.get_last_name())
    print(human.get_date_of_birth())
    print(human.get_contact_number())
    print(human.get_city())
    print(human.get_country())
    print(human.get_address())

    human.set_first_name('aaa')
    human.set_last_name('bbb')
    human.set_date_of_birth('2005-05-10')
    human.set_contact_number('123456789')
    human.set_city('Wroclaw')
    human.set_country('POLSKA')
    human.set_address('aaabbb 123 12-123 Wroclaw')

    print('')
    print(human.get_first_name())
    print(human.get_last_name())
    print(human.get_date_of_birth())
    print(human.get_contact_number())
    print(human.get_city())
    print(human.get_country())
    print(human.get_address())

    city = City.create_class_from_input()
    print(city.get_city_info())