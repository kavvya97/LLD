class InternalRequest:
    def __init__(self, dest_floor, src_elevator_id):
        self.dest_floor = dest_floor
        self.src_elevator_id = src_elevator_id

    def get_dest_floor(self):
        return self.dest_floor

    def set_dest_floor(self, dest_floor):
        self.dest_floor = dest_floor

    def get_src_elevator_id(self):
        return self.src_elevator_id

    def set_src_elevator_id(self, src_elevator_id):
        self.src_elevator_id = src_elevator_id
