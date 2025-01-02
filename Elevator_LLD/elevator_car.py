from elevator_controller import ElevatorController
from elevator_state import ElevatorState
class ElevatorCar:
    def __init__(self, id, capacity=10, ) -> None:
        self.elevator_id = id
        self.capacity = capacity
        self.elevator_state = ElevatorState()
        self.controller = ElevatorController(id, self.elevator_state)

    def moveToFloor(self, destination_floor):
        self.controller.move_elevator_to_floor(destination_floor)