class Player:
    def __init__(self, pname, isWhite, isCurPlayer, isHuman):
        self.pname = pname
        self.isWhite = isWhite
        self.isCurPlayer = isCurPlayer
        self.isHuman = isHuman

    def get_player_name(self):
        return self.pname
    
    def is_player_white(self):
        return self.isWhite
    
    def isHumanPlayer(self):
        return self.isHuman
    
    def isPlayerTurn(self):
        return self.isCurPlayer