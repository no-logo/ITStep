class BankAccount:

    def __init__(self, account_number, balance) -> None:
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def blance(self):
        return self.__balance
    
    @blance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value
        else:
            raise ValueError('balance must be positive')
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transaction_fee(self)
        pass
    # daw procent prowizji