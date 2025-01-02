class Board:
    def __init__(self, snakes, ladders, size):
        self.snakes = snakes
        self.ladders = ladders
        self.size = size

    def is_snake(self, pos):
        return pos in self.snakes
    
    def is_ladder(self, pos):
        return pos in self.ladders
    
    def get_snake_tail(self, pos: int) -> int:
        return self.snakes[pos]

    def get_ladder_end(self, pos: int) -> int:
        return self.ladders[pos]
    
    def get_final_position(self, new_pos):
        if self.is_ladder(new_pos):
            return self.get_ladder_end(new_pos)
        elif self.is_snake(new_pos):
            return self.get_snake_tail(new_pos)
        else:
            return new_pos

    