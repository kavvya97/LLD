from constants import ElevatorControllerStrategy, ElevatorDirection, ElevatorStatus
from firstcomefirstserve import FirstComeFirstServe
from strategy.lookupalgorithm import LookUpAlgorithmStrategy
from strategy.shortestseektime import shortestSeekTimeStrategy
class ElevatorControlStrategy:
    def __init__(self, floor_num, strategy) -> None:
        self.floor_num = floor_num
        self.strategy = strategy
    
    def determine_next_stop(self, floor_num):
        if self.strategy == ElevatorControllerStrategy.FIRST_COME_FIRST_SERVE:
            return FirstComeFirstServe().determine_next_stop(floor_num)
        elif self.strategy == ElevatorControllerStrategy.LOOK_AHEAD:
            return LookUpAlgorithmStrategy().determine_next_stop(floor_num)
        else:
            return shortestSeekTimeStrategy().determine_next_stop(floor_num)
