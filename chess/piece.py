from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, isKilled=False, isWhite=False):
        self.isKilled = isKilled
        self.isWhite = isWhite

    def set_isKilled(self, isKilled):
        self.isKilled = isKilled

    def set_isWhite(self, isWhitePiece):
        self.isWhite = isWhitePiece
    
    @abstractmethod
    def can_move():
        pass

    @abstractmethod
    def get_symbol():
        pass

    @abstractmethod()
    def move():
        pass