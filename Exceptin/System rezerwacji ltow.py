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
        pass

    def cancel_flight_reservations(self, flight_number, nuber_of_places):
        pass

    def check_avalibility(self, flight_number):
        try:
            if flight_number != self._flight_number:
                raise FlightNotFoudError
        
        