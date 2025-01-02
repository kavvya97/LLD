from player import Player
from board import Board
from gameStatus import GameStatus
from move import Move

class Game:
    def __init__(self, p1, p2):
        self.players = [p1, p2]
        self.board = Board()
        self.currentPlayer = None
        self.status = GameStatus.ACTIVE
        self.movesPlayed = []
        self.currMoveIndex = 0

        self.board.reset_board()
        self.display_game_board()
        self.currMoveIndex = 0

    def display_game_board(self):
        self.board.display_board()

    def get_spot_position(self, spot):
        spotRow = 8 - int(spot[0])
        spotCol = ord(spot[1]) - ord('a')
        return [spotRow, spotCol]

    def process_move(self, curr_player, start, end):
        start_move = self.get_spot_position(start)
        end_move = self.get_spot_position(end)

        start_spot = self.board.get_spot(start_move[0], start_move[1])
        end_spot = self.board.get_spot(end_move[0], end_move[1])
        curr_piece = start_spot.piece

        move = Move(curr_player, start_spot, end_spot, curr_piece)

        if curr_piece.can_move(self.board, start_spot, end_spot):
            curr_piece.move(self.board, start_spot, end_spot)
            end_spot.piece = curr_piece
            start_spot.piece = None
            self.currMoveIndex += 1
        else:
            move.set_invalid_move()

        self.movesPlayed.append(move)

        self.board.display_board()
        return True

    def undo(self):
        self.currMoveIndex -= 1
        last_move = self.movesPlayed[self.currMoveIndex]
        if last_move is not None:
            last_move.pieceMoved.move(self.board, last_move.endSpot, last_move.startSpot)
            last_move.startSpot.piece = last_move.pieceMoved
            last_move.endSpot.piece = last_move.pieceKilled
            self.board.display_board()

    def redo(self):
        # Perform redo just like undo
        self.currMoveIndex += 1
