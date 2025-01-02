
from spot import Spot
from piece import Piece

class Move:
    def __init__(self, player, startSpot: Spot, endSpot: Spot, pieceMoved: Piece, pieceKilled: Piece) -> None:
        self.player = player
        self.startSpot = startSpot
        self.endSpot = endSpot
        self.pieceMoved = pieceMoved
        self.pieceKilled = pieceKilled
        self.isValidMove = False
        self.castiling = False
    
    def isCastlingMove(self):
        return self.castlingMove

    def setCastlingMove(self, castlingMove):
        self.castlingMove = castlingMove

    def setInvalidMove(self):
        self.isValidMove = False

    def getPlayer(self):
        return self.player

    def getStartSpot(self):
        return self.startSpot

    def getEndSpot(self):
        return self.endSpot

    def getPieceMoved(self):
        return self.pieceMoved

    def getPieceKilled(self):
        return self.pieceKilled
