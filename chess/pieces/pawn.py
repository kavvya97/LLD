from piece import Piece
from board import Board
from spot import Spot

class Pawn(Piece):
    def __init__(self, isKilled=False, isWhite=False):
        super().__init__(isKilled, isWhite)

    def get_symbol():
        return 'PAWN'
    
    def can_move(board: Board, start: Spot, end: Spot):
        # Considering the start and end spot, check if the bishop can move 
        # check if another piece in-between, in which case, it cannot move
        return True

    def move(board: Board, start: Spot, end: Spot):
        # Logic to move the bishop piece
        pass