from spot import Spot
from pieces import rook, bishop, king, knight, queen, pawn

class Board:
    def __init__(self):
        self.boxes = [[None for _ in range(8)] for _ in range(8)]
        self.reset_board()

    def get_spot(self, row, col):
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            print("Error: Index out of bounds")
            return None
        return self.boxes[row][col]

    def reset_board(self):
        # Initialize white pieces
        self.boxes[0][0] = Spot(0, 0, rook(isWhite=True))
        self.boxes[0][1] = Spot(0, 1, knight(isWhite=True))
        self.boxes[0][2] = Spot(0, 2, bishop(isWhite=True))
        self.boxes[0][3] = Spot(0, 3, queen(isWhite=True))
        self.boxes[0][4] = Spot(0, 4, king(isWhite=True))
        self.boxes[0][5] = Spot(0, 5, bishop(isWhite=True))
        self.boxes[0][6] = Spot(0, 6, knight(isWhite=True))
        self.boxes[0][7] = Spot(0, 7, rook(isWhite=True))

        for i in range(8):
            self.boxes[1][i] = Spot(1, i, pawn(isWhite=True))

        # Initialize black pieces
        self.boxes[7][0] = Spot(7, 0, rook(isWhite=False))
        self.boxes[7][1] = Spot(7, 1, knight(isWhite=False))
        self.boxes[7][2] = Spot(7, 2, bishop(isWhite=False))
        self.boxes[7][3] = Spot(7, 3, queen(isWhite=False))
        self.boxes[7][4] = Spot(7, 4, king(isWhite=False))
        self.boxes[7][5] = Spot(7, 5, bishop(isWhite=False))
        self.boxes[7][6] = Spot(7, 6, knight(isWhite=False))
        self.boxes[7][7] = Spot(7, 7, rook(isWhite=False))

        for i in range(8):
            self.boxes[6][i] = Spot(6, i, pawn(isWhite=False))

        # Initialize remaining boxes without any piece
        for i in range(2, 6):
            for j in range(8):
                self.boxes[i][j] = Spot(i, j, None)

    def display_board(self):
        print("%12s" % "", end="")
        for ch in range(ord('a'), ord('h') + 1):
            print("%12c" % ch, end="")
        print()

        for i in range(8):
            print("%12d" % (8 - i), end="")
            for j in range(8):
                spot = self.get_spot(i, j)
                if spot.piece is not None:
                    symbol = "WHITE" + spot.piece.symbol if spot.piece.is_white else "BLACK" + spot.piece.symbol
                    print("%12s" % symbol, end="")
                else:
                    print("%12s" % ".", end="")
            print("%12d" % (8 - i))

        print("%12s" % "", end="")
        for ch in range(ord('a'), ord('h') + 1):
            print("%12c" % ch, end="")
        print("\n")
