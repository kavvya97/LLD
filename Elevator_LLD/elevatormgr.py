from elevator_car import ElevatorCar
import threading
from typing import List
class ElevatorManager:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            cls._lock.acquire()
            cls._instance = super().__new__(cls)
            cls._lock.release()
        return cls._instance
    
    def __init__(self, no_of_elevators: List[dict]) -> None:
        self.no_of_elevators = no_of_elevators
        self.elevators = {}

    def initialize_elevators(self):
        for elevator_id in self.no_of_elevators:
            self.elevators[elevator_id] = ElevatorCar(elevator_id)
        
    def get_elevator(self, elevator_id):
        return self.elevators[elevator_id]