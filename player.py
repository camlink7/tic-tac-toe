import math

class Player:
    def __init__(self, game, letter):
        self.game = game
        self.letter = letter


class ComputerPlayer(Player):
    def __init__(self, game, letter):
        super().__init__(game, letter)

