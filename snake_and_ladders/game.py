from typing import List
from player import Player
from board import Board
from dice import Dice
class SnakeAndLadderGame:
    def __init__(self, players, board: Board, dice: Dice):
        self.players = []
        self.board = board
        self.dice = dice
        for player in players:
            self.players.append(Player(player, 0))

    def play_turn(self):
        player_num = 0
        while True:
            player = self.players[player_num]
            dice_roll = self.dice.roll_dice()

            print(f"{player.name}'s turn (rolling dice...)")
            print(f"{player.name} rolled {dice_roll}")

            new_position = player.get_position() + dice_roll

            if new_position > self.board.size:
                print(f"{player.name} cannot move beyond position ${self.board.size * self.board.size}. His turn is skipped.")
                final_position =  player.get_position()
            else:
                final_position = self.board.get_final_position(new_position)
                print(f"{player.name} current position: {final_position}")
                player.set_position(final_position)
            print('\n')

            # Player has won the game
            if final_position == self.board.size:
                print(f'Player {player.name} has won the game!')
                return
            # algorithm to provide each player a chance
            player_num += 1
            player_num = player_num % len(self.players)
