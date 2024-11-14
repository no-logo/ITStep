class AgeDescriptor:
    def __init__(self) -> None:
        self._age = 0

    def __get__(self, instance, owner):
        return self._age
    
    def __set__(self, instance, age):
        if age < 18 or age > 100:
            raise ValueError('wiek spoza zakresu')
        else:
            self._age = age
        
class SalaryDescriptor:
    def __init__(self) -> None:
        self._salary = 0

    def __get__(self, instance, owner):
        return self._salary
    
    def __set__(self, instance, salary):
        if salary < 2000:
            raise ValueError("zbyt niskie wynagrodzenie")
        else:
            self._salary = salary

class Employee:
    age = AgeDescriptor()
    salary = SalaryDescriptor()

    def __init__(self, employee_name, employee_age, employee_salary) -> None:
        self.name = employee_name
        self.age = employee_age
        self.salary = employee_salary

e = Employee('Andrzej', 20, 2500)
print(e.name)
print(e.age)
print(e.salary)