from piece import Piece
class Spot:

    def __init__(self, row, col, piece:Piece) -> None:
        self.row = row
        self.col = col
        self.piece = piece

    def get_piece(self):
        return self.piece
    
    def set_piece(self, piece: Piece):
        self.piece = piece

    def get_pos(self):
        return (self.row, self.col)
    
    def set_pos(self, pos):
        (self.row, self.col) = pos