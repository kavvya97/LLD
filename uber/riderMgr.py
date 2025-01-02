import threading
from rider import Rider

class RiderMgr:
    riderMgr_instance = None
    mtx = threading.Lock()
    def __init__(self):
        self.riders = {}

    @staticmethod
    def get_rider_manager_instance():
        if RiderMgr.riderMgr_instance is None:
            with RiderMgr.mtx:
                if RiderMgr.riderMgr_instance is None:
                    RiderMgr.riderMgr_instance = RiderMgr()
        return RiderMgr.riderMgr_instance

    def add_rider(self, rider: Rider):
        self.riders[rider.getRiderId()] = rider
    
    def get_rider(self, rider_id: int):
        return self.riders[rider_id]
