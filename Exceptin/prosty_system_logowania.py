
class AuthenticationError(Exception):
    pass

class TooManyAttmptsError(Exception):
    pass

class System():
    def __init__(self, user_name, password) -> None:
        self._user_name = user_name
        self._password = password
        self._number_of_attempts = 0

    def system_login(self, user_name, password):
        x = 0
        
        if self._user_name != user_name or self._user_name != user_name:
            self._number_of_attempts += 1
            if self._number_of_attempts >= 3:
                raise TooManyAttmptsError
            raise AuthenticationError
        else:
            print('Access Granted')
            x = 1
        return x

system = System("Andrzej", 123)

def main():
    while True:
        try:
            user = input("Podaj nazwę użytkownika: ")
            password = input("Podaj hasło: ")
            access = system.system_login(user, password)
            if access:
                break
        except AuthenticationError as e:
            print(f'Zły login lub hasło: {e}')
        except TooManyAttmptsError as e:
            print(f'Zbyt wiele nieudanych prób: {e}')
            break
        except Exception as e:
            print(f'nieznany błąd: {e} ')
        finally:
            print('Proces logownia zakończony')

if __name__ == '__main__':
    main()
    




        
        

    