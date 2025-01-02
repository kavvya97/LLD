import threading

class ParkingLot:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):

        if not cls._instance:
            cls._lock.acquire()
            cls._instance = super().__new__(cls)
            cls._lock.release()
        return cls._instance
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
