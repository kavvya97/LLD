from enum import Enum

class VehicleType(Enum):
    ELECTRIC, HEAVY, NORMAL = 1,2,3

class ParkingLotType(Enum):
    HANDICAPPED, ELECTRIC, HEAVY, NORMAL = 1,2,3,4

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3

class Address:
    def __init__(self, location, zip_code, state, country, streetAddress):
        pass

class Person:
    def __init__(self, name, phone, email):
        pass
