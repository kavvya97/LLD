from .constants import  *
from .parking_display_board import *

class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}
        self.__info_portals = {}
        self.__free_handicapped_spot_count = {'free_spot': 0}
        self.__free_compact_spot_count = {'free_spot': 0}
        self.__free_large_spot_count = {'free_spot': 0}
        self.__free_motorbike_spot_count = {'free_spot': 0}
        self.__free_electric_spot_count = {'free_spot': 0}
        self.__display_board = ParkingDisplayBoard()

    def add_parking_spot(self, spot):
        if spot.get_type() == ParkingLotType.HANDICAPPED:
            self.__handicapped_spots[spot.get_number()] = spot
    
    def assignVehicleToSpot(self, vehicle, spot):
        spot.assign_vehicle()
        if vehicle.get_type() == VehicleType.ELECTRIC:
            self.updateDisplayBoardForElectric(spot)
        pass

    def update_display_board_for_handicapped(self, spot):
        if self.__display_board.get

