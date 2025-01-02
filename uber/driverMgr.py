import threading
from driver import Driver
class DriverMgr:

    driverMgr_instance = None
    mtx = threading.Lock()
    def __init__(self):
        self.drivers = {}
    @staticmethod
    def get_driver_manager_instance():
        if DriverMgr.driverMgr_instance is None:
            with DriverMgr.mtx:
                if DriverMgr.driverMgr_instance is None:
                    DriverMgr.driverMgr_instance = DriverMgr()
        return DriverMgr.driverMgr_instance

    def add_driver(self, driver: Driver):
        self.drivers[driver.driver_id] = driver
    
    def get_driver(self, driver_id: int):
        return self.drivers[driver_id]
    
    def get_drivers_map(self):
        return self.drivers