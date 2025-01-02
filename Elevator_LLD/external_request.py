"""
select wheterh you weant to go UP/DOWN
src_floor
"""
from constants import ElevatorDirection
class ExternalRequest:
    def __init__(self, direction: ElevatorDirection, floor):
        self.direction_to_go = direction
        self.src_floor = floor

    def get_direction(self):
        return self.direction_to_go

    def set_direction(self, direction: ElevatorDirection):
        self.direction_to_go = direction

    def get_src_floor(self):
        return self.src_floor

    def set_src_floor(self, floor):
        self.src_floor = floor