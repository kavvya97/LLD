from elevatormgr import ElevatorManager
from external_request_processor import ExternalRequestProcessor
from internal_request_processor import InternalRequestProcessor
from external_request import ExternalRequest
from internal_request import InternalRequest
from constants import ElevatorDirection, ElevatorStatus
class ElevatorSystem:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, no_of_floors, no_of_elevators):
        self.no_of_floors = no_of_floors
        self.no_of_elevators = no_of_elevators

        # initialize the elevators
        elevatormgr = ElevatorManager(self.no_of_elevators)
        elevatormgr.initialize_elevators()
        
        self.extReqProcessor = ExternalRequestProcessor()
        self.intReqProcessor = InternalRequestProcessor()

    def setExternalRequest(self, direction, src_floor):
        externalRequest = ExternalRequest(direction, src_floor)
        self.extReqProcessor.process_external_request(external_request=externalRequest)

    def setInternalRequest(self, dest_floor, elevator_id):
        internalRequest = InternalRequest(dest_floor, elevator_id)
