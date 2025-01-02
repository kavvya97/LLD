from constants import BoxSize
class Box:
    def __init__(self, size: BoxSize, box_id) -> None:
        self.size = size
        self.box_id = box_id
        self.available = True
    
    def get_box_size(self):
        return self.size
    
    def allocate_box(self):
        self.available = False

    def get_box_id(self):
        return self.box_id