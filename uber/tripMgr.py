import threading
from tripMetaData import TripMetaData
from strategyMgr import StrategyMgr
from trip import Trip
from location import Location
from rider import Rider
class TripManager:
    
    
    tripMgrInstance = None
    mtx = threading.Lock()
    def __init__(self) -> None:
        self.trips = {}
        self.tripMetaData = {}
    
    @staticmethod
    def get_tripMgr_instance():
        if TripManager.tripMgrInstance is None:
            with TripManager.mtx:
                if TripManager.tripMgrInstance is None:
                    TripManager.tripMgrInstance = TripManager()
        return TripManager.tripMgrInstance
    
    def create_trip(self, srcLoc: Location, dstLoc: Location, rider: Rider):
        tripMetaData = TripMetaData(srcLoc, dstLoc, driver_rating=None, rider_rating=rider.rating)
        strategyMgr = StrategyMgr.get_strategyMgr_instance()
        driver = strategyMgr.determine_drive_matching_strategy(tripMetaData)
        tripMetaData.set_driver_rating(driver.rating)
        price = strategyMgr.determine_price_matching_strategy(tripMetaData)
        trip = Trip(srcLoc, dstLoc, price, driver, rider, tripMetaData)
        self.trips[trip.get_trip_id()] = trip
        self.tripMetaData[trip.get_trip_id()] = tripMetaData

    def get_trips_map(self):
        return self.trips
    
    def get_trip_details(self, tripId):
        return self.trips[tripId]


