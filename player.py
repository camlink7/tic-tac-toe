import math

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        return input()

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

class HumanPlayer(Player):
    def __init(self, letter):
        super().__init__(letter)
