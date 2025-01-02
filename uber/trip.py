import threading
from tripMetaData import TripMetaData
from strategyMgr import StrategyMgr
from location import Location
from driver import Driver
from rider import Rider
class Trip:
    next_trip_id = 1
    def __init__(self, srcLoc: Location, dstLoc: Location, price, driver: Driver, rider: Rider, tripMetaData: TripMetaData) -> int:
        self.src_loc = srcLoc
        self.dst_loc = dstLoc
        self.price = price
        self.driver = driver
        self.rider = rider 
        self.trip_metadata = tripMetaData
        self.strategy_mgr = StrategyMgr()
        self.trip_id = Trip.next_trip_id
        Trip.next_trip_id += 1
    
    def get_trip_id(self) -> int:
        return self.trip_id

    def display_trip_details(self):
        print("Trip id -", self.trip_id)
        print("Rider -", self.rider.getRiderName())
        print("Driver -", self.driver.getDriverName())
        print("Price -", self.price)
        print("Locations - {},{} and {},{}".format(self.src_loc.lat, self.src_loc.long,
                                                   self.dst_loc.lat, self.dst_loc.long))