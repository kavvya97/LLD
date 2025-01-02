# from jumper import Snake, Ladder
from game import SnakeAndLadderGame
from player import Player
from board import Board
from dice import Dice

def main():

    ladders = {
        1: 38,
        4: 14,
        9: 31,
        21: 42,
        28: 84,
        36: 44,
        51: 67,
        71: 91,
        80: 100
    }

    snakes = {
        98: 78,
        95: 75,
        93: 73,
        87: 24,
        64: 60,
        62: 19,
        56: 53,
        49: 11,
        48: 26
    }

    # Define players
    num_players = int(input("How many players are playing? "))
    player_names = []
    for i in range(num_players):
        name = input("Enter player " + str(i+1) + " name: ")
        player_names.append(name)
    print("\n")

    # Create board and dice
    board = Board(snakes, ladders, size=100)
    dice = Dice(number_of_dice=1, strategy='crooked')

    # Create and start the game
    game = SnakeAndLadderGame(player_names, board, dice)
    game.play_turn()

if __name__ == "__main__":
    main()
