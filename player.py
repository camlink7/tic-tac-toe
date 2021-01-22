import math
import random
from move import Move

class Player:
    def __init__(self, letter):
        self.letter = letter
        self.game = None

    def get_move(self):
        return input()

    def set_game(self, game):
        self.game = game

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

