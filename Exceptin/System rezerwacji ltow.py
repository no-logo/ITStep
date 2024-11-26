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
            print(fnf)
        except NoReservationError as nre:
            print(nre)

    
                
        
flight = Flight(123,10,0)
print(flight.check_avalibility(123))
flight.flight_reservation(123,3)
print(flight.check_avalibility(123))
flight.cancel_flight_reservations(123,2)
print(flight.check_avalibility(123))
