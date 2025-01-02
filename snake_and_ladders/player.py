class Player:
    def __init__(self, name, position=0) -> None:
        self.name = name
        self.position = position

    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position
    