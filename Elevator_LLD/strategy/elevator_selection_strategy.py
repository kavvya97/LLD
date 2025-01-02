from constants import  ElevatorSelectionStrategy
from strategy import zone_selection_strategy, odd_even_selection_strategy
class ElevatorSelectionStategy:
    def __init__(self,strategy) -> None:
        self.strategy = strategy
    
    def select_elevator(self, external_request):
        if self.strategy == ElevatorSelectionStrategy.ODD_EVEN_SELECTION:
            return odd_even_selection_strategy().determine_elevator(external_request)
        else:
            return zone_selection_strategy().determine_elevator(external_request)
