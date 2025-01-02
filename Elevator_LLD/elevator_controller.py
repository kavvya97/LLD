from elevator_car import ElevatorCar
from elevator_state import ElevatorState
from strategy.elevator_control_strategy import ElevatorControlStrategy
from constants import ElevatorDirection, ElevatorStatus, ElevatorControllerStrategy
class ElevatorController:
    def __init__(self, id, state: ElevatorState) -> None:
        self.controller_id = id
        self.elevator_state = state
        
    def move_elevator_to_floor(self, floor_no, strategy=ElevatorControllerStrategy.FIRST_COME_FIRST_SERVE):
        next_floor = ElevatorControlStrategy().determineNextStop(floor_no, strategy)
        if next_floor > self.elevator_state.get_cur_floor():
            self.elevator_state.set_cur_direction(ElevatorDirection.UP)
        elif next_floor < self.elevator_state.get_cur_floor():
            self.elevator_state.set_cur_direction(ElevatorDirection.DOWN)
        if next_floor != self.elevator_state.get_cur_floor():
            self.elevator_state.set_cur_state(ElevatorStatus.MOVING)