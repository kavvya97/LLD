from internal_request import InternalRequest
from elevatormgr import ElevatorManager
class InternalRequestProcessor:
    def process_internal_request(internalrequest: InternalRequest):
        elevator_id = internalrequest.get_src_elevator_id()
        assignedElevator = ElevatorManager.get_elevator(elevator_id=elevator_id)
        assignedElevator.moveToFloor(internalrequest.get_dest_floor())
