from dice_roll_strategy import DiceRollStrategy
class Dice:
    def __init__(self, number_of_dice=1, strategy='fair'):
        self.number_of_dice = number_of_dice
        self.strategy = strategy
    
    def get_total_dice(self):
        return self.number_of_dice
    
    def roll_dice(self):
        return sum(DiceRollStrategy().roll_dice(self.strategy) for _ in range(self.number_of_dice))
    