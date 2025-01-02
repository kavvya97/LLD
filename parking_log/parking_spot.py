from constants import *

from abc import ABC


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__free = True
        self.__vehicle = None
        self.__parking_spot_type = parking_spot_type

    def is_free(self):
        return self.__free

    
    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.free = True

class HandicappedParkingSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingLotType.HANDICAPPED)

class ElectricParkingSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingLotType.ELECTRIC)