from enum import Enum

class ElevatorDirection(Enum):
    NONE, UP, DOWN = 0, 1, 2

class ElevatorStatus(Enum):
    MOVING, STOPPED, IDLE = 0, 1, 2

class  ElevatorControllerStrategy(Enum):
    FIRST_COME_FIRST_SERVE, LOOK_AHEAD, SCAN_AHEAD, SHORTEST_SEEK_TIME = 0, 1, 2, 3

class ElevatorSelectionStrategy(Enum):
    ODD_EVEN_SELECTION, ZONE_BASED_SELECTION = 0, 1