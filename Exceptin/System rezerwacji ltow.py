fileName = 'logs.txt'
from datetime import date
from datetime import datetime


class FlightFullError(Exception):
    pass

class NoReservationError(Exception):
    pass

class FlightNotFoudError(Exception):
    pass

class Flight:
    def __init__(self, flight_number, capacity, reservations) -> None:
        self._flight_number = flight_number
        self._capacity = capacity
        self._reservations = reservations

    def check_avalibility(self, flight_number):
        x = 0
        try:
            if flight_number != self._flight_number:
                raise FlightNotFoudError("Flight number not exists")
            else:
                if self._capacity > self._reservations:
                    x = self._capacity - self._reservations
                    return x
                else:
                    return x
        except FlightNotFoudError as e:
            with open(fileName, 'a') as logfile:  
                logfile.write(f'[{datetime.now()}] {e}\n')
            print(e)
        return x


    def flight_reservation(self, flight_number, nuber_of_places):
        av = self.check_avalibility(flight_number)
        try:
            if av >= nuber_of_places:
                self._reservations += nuber_of_places
            else:
                raise FlightFullError(f'Only {av} places are available')
        except FlightFullError as e:
            with open(fileName, 'a') as logfile:  
                logfile.write(f'[{datetime.now()}] {e}\n')
            print(e)

    def cancel_flight_reservations(self, flight_number, nuber_of_places):
        try:
            if self._flight_number != flight_number:
                raise FlightNotFoudError("Flight number not exists")
            if self._reservations < nuber_of_places:
                raise NoReservationError("Too much places to cancel")
            else:
                self._reservations -= nuber_of_places
                print("Reservations canceled")
        except FlightNotFoudError as fnf:
            with open(fileName, 'a') as logfile:  
                logfile.write(f'[{datetime.now()}] {fnf}\n')
            print(fnf)
        except NoReservationError as nre:
            with open(fileName, 'a') as logfile:  
                logfile.write(f'[{datetime.now()}] {nre}\n')
            print(nre)

    
with open(fileName, 'w') as logfile:              
    flight = Flight(123,10,0)
    logfile.write(f'[{datetime.now()}] 1 ustawienie nr lotu {flight._flight_number} ilosci miejsc {flight._capacity} oraz rezerwacji {flight._reservations}\n')

with open(fileName, 'a') as logfile:  
    #print(flight.check_avalibility(123))
    logfile.write(f'[{datetime.now()}] 2 sprawdzenie ilosci dostepnych miejsc {flight.check_avalibility(123)}\n')
    #flight.flight_reservation(123,11)
    logfile.write(f'[{datetime.now()}] 3 rezerwacja 11 miejsc {flight.flight_reservation(123,11)}\n')
    #print(flight.check_avalibility(123))
    logfile.write(f'[{datetime.now()}] 4 sprawdzenie ilosci dostepnych miejsc {flight.check_avalibility(123)}\n')
    #flight.cancel_flight_reservations(123,2)
    logfile.write(f'[{datetime.now()}] 5 rezerwacja 2 miejsc {flight.flight_reservation(123,2)}\n')
    #print(flight.check_avalibility(123))
    logfile.write(f'[{datetime.now()}] 6 sprawdzenie ilosci dostepnych miejsc {flight.check_avalibility(123)}\n')





