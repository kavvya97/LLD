from locker import Locker
from package import Package
from strategy.nearestLockerToPackageStrategy import NearestLockerStrategy
class LockerMgr:
    _LockerMgrInstance = None
    _mtx = None

    def __init__(self):
        self.lockers = []
    
    @staticmethod
    def get_locker_mgr_instance():
        if LockerMgr._LockerMgrInstance is None:
            with LockerMgr._mtx:
                if LockerMgr._LockerMgrInstance is None:
                    LockerMgr._LockerMgrInstance = LockerMgr()
        return LockerMgr._LockerMgrInstance
    

    def add_lockers(self, locker: Locker):
        self.lockers.append(locker)

    def remove_lockers(self, locker: Locker):
        self.lockers.remove(locker)

    # returns Locker ID
    def assign_locker_to_package(package: Package, strategy=None):
        return NearestLockerStrategy().determine_locker(package)
