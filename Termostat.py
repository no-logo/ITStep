class Thermostat:
    
    def __init__(self, temperature) -> None:
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, t):
        if t >= - 30 and t <= 50:
            self.__temperature = t
        else:
            raise ValueError('temperatura not in scope')
        
    @property
    def temperature_farenheit(self):
        return self.__temperature * 9 / 5 + 32
    
    @property
    def temperature_kelvin(self):
        return self.__temperature + 273.15
    
    @temperature_kelvin.setter
    def temperature_kelvin(self, tk):
        if isinstance(tk, float) or isinstance(tk, int):
            self.__temperature = tk - 273.15
        else:
            raise ValueError('temperature must be int or float')


term = Thermostat(10)
term.temperature = 10
print(term.temperature)
print(term.temperature_farenheit)
print(term.temperature_kelvin)
term.temperature_kelvin = 273.15
print(term.temperature_kelvin)
print(term.temperature)