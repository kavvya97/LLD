from constants import ElevatorDirection, ElevatorStatus

class ElevatorState:
    def __init__(self, cur_floor=0, current_direction=ElevatorDirection.NONE, cur_status=ElevatorStatus.IDLE) -> None:
        self._cur_floor = cur_floor
        self._cur_direction = current_direction
        self._cur_state = cur_status

    def get_cur_floor(self):
        return self._cur_floor

    def set_cur_floor(self, new_floor):
        self._cur_floor = new_floor

    def get_cur_direction(self):
        return self._cur_direction

    def set_cur_direction(self, new_direction):
        self._cur_direction = new_direction

    def get_cur_state(self):
        return self._cur_state

    def set_cur_state(self, new_state):
        self._cur_state = new_state
