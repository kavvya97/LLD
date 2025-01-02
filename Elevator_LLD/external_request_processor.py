
from constants import ElevatorSelectionStrategy
from elevator_state import ElevatorState
from external_request import ExternalRequest
from strategy import elevator_selection_strategy
from elevatormgr import ElevatorManager

class ExternalRequestProcessor:

    def __init__(self, strategy=ElevatorSelectionStrategy.ODD_EVEN_SELECTION):
        self.strategy = strategy

    def process_external_request(strategy, external_request: ExternalRequest):
        elevator_id = ElevatorSelectionStrategy(strategy).select_elevator(external_request)
        elevator_mgr = ElevatorManager()
        assigned_elevator = elevator_mgr.get_elevator(elevator_id)
        assigned_elevator.moveToFloor(external_request.get_src_floor())
        
        