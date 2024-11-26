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

    def flight_reservation(self, flight_number, nuber_of_places):
        av = self.check_avalibility(self, flight_number)
        try:
            if av >= nuber_of_places:
                self._reservations += nuber_of_places
            else:
                raise FlightFullError(f'Only av places are available')
        except FlightFullError as e:
            print(e)

    def cancel_flight_reservations(self, flight_number, nuber_of_places):
        try:
            if self._flight_number != flight_number:
                raise FlightNotFoudError("Flight number not exists")
            if self._reservations < nuber_of_places:
                raise NoReservationError("Too much places to cancel")
            else:
                self._reservations - nuber_of_places
                print("Reservations canceled")
        except FlightNotFoudError as fnf:
            print(fnf)
        except NoReservationError as nre:
            print(nre)

    def check_avalibility(self, flight_number):
        try:
            if flight_number != self._flight_number:
                raise FlightNotFoudError("Flight number not exists")
            else:
                if self._capacity > self._reservations:
                    return self._capacity - self._reservations
                else:
                    return 0
        except FlightNotFoudError as e:
            print(e)

                
        
        