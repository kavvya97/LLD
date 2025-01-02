# Strategy Design Pattern
import random
class DiceRollStrategy:
    def roll_dice(self, cur_strategy="fair"):
        if cur_strategy == "fair":
            return FairDiceRollStrategy().roll_dice()
        # crooked strategy
        else:
            return CrookedDiceRollStrategy().roll_dice()


class FairDiceRollStrategy:
    def roll_dice(self) -> int:
        return random.randint(1, 6)

class CrookedDiceRollStrategy:
    def roll_dice(self) -> int:
        p = random.random()
        if p < 0.3:
            return random.choices([1,3,5])
        else:
            return random.randint(1, 3) * 2
