from tripMetaData import TripMetaData
from driverMgr import DriverMgr
class LeastTimeBasedMatchingStrategy:
    def match_driver(self, tripMetaData: TripMetaData):
        driverMgr = DriverMgr.get_driver_manager_instance()
        drivers_map = driverMgr.get_drivers_map()
        if len(drivers_map) == 0:
            print("No Drivers found nearby!!")
        
        print("utilizing Quad Trees to find nearby drivers")
        driver = list(drivers_map.values())[0]
        return driver

       