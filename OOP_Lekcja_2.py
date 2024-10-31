

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

    def info(self):
        return f'first name: {self.__first_name}, last_name: {self.__last_name}'


class Builder(Human):
    def __init__(self, first_name, last_name, date_of_birth, contact_number, city, country, address,stanowisko,nazwa_firmy) -> None:
        super().__init__(first_name, last_name, date_of_birth, contact_number, city, country, address)
        self.__stanowisko = stanowisko
        self.__nazwa_firmy = nazwa_firmy

    def get_stanowisko(self):
        return self.__stanowisko
    def get_nazwa_firmy(self):
        return self.__nazwa_firmy
    
    def set_stanowisko(self, stanowisko):
        self.__stanowisko = stanowisko
    
    def set_nazwa_firmy(self, nazwa_firmy):
        self.__nazwa_firmy

    def info(self):
        return f'first name: {self.get_first_name()}, last_name: {self.get_last_name()}, stanowisko: {self.__stanowisko}, nazwa firmy: {self.__nazwa_firmy}'
    

class Sailor(Human):
    def __init__(self, first_name, last_name, date_of_birth, contact_number, city, country, address, stopien, nazwa_jachtu) -> None:
        super().__init__(first_name, last_name, date_of_birth, contact_number, city, country, address)
        self.__stopien = stopien
        self.__nazwa_jachtu = nazwa_jachtu

    def get_stopien(self):
        return self.__stopien
    
    def get_nazwa_jachtu(self):
        return self.__nazwa_jachtu
    
    def set_stopien(self, stopien):
        self.__stopien = stopien

    def set_nazwa_jachtu(self, nazwa_jachtu):
        self.__nazwa_jachtu = nazwa_jachtu

    def info(self):
        return f'first name: {self.get_first_name()}, last_name: {self.get_last_name()}, stopień: {self.__stopien}, nazwa jachtu: {self.__nazwa_jachtu}'
    
    
class Pilot(Human):
    def __init__(self, first_name, last_name, date_of_birth, contact_number, city, country, address, nazwa_linii_lotniczych, typ_samolotu) -> None:
        super().__init__(first_name, last_name, date_of_birth, contact_number, city, country, address)
        self.__nazwa_linii_lotniczych = nazwa_linii_lotniczych
        self.__typ_samolotu = typ_samolotu

    def get_nazwa_linii_lotniczych(self):
        return self.__nazwa_linii_lotniczych
    
    def get_typ_samolotu(self):
        return self.__typ_samolotu
    
    def set_nazwa_linii_lotniczych(self, nazwa_linii_lotniczych):
        self.__nazwa_linii_lotniczych = nazwa_linii_lotniczych

    def set_typ_samolotu(self, typ_samolotu):
        self.__typ_samolotu = typ_samolotu

    def info(self):
        return f'first name: {self.get_first_name()}, last_name: {self.get_last_name()}, nazwa linii lotniczych: {self.__nazwa_linii_lotniczych}, typ samolotu: {self.__typ_samolotu}'
    


    
    s = Sailor('Andrzej', 'Wawryk', '1975-01-03', '536956536', 'Kraków', 'Polska', 'Ulica 1/23 12-345 Kraków','Jachtowy Sternik Morski', 'Gedania')
    print()
    print(s.info())
    print()

    


class X:
    def __init__(self):
        print('X init')

class Y(X):
    def __init__(self):
        super().__init__()
        print('Y init')

class Z(X):
    def __init__(self):
        super().__init__()
        print('Z init')

class A(Y, Z):
    def __init__(self):
        super().__init__()
        print('A init')

a = A()