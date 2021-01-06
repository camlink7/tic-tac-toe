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
    
    '''def get_move(self):
        self.copy = self.game 
        self.winning_spot_not_found = True
        self.winning_spots = []
        self.available_spots = self.copy.get_available_spots()
        #return(random.choice(self.game.get_available_spots()))
        while (self.winning_spot_not_found):
            for i in range(0, len(self.available_spots)):
                new_move = self.copy.process_input(self.available_spots[i])
                self.copy.update_spot(new_move.r_spot, new_move.c_spot)
            if self.copy.game_winner == self:
               self.winning_spots.append[self.available_spots[0]]
            else:
                self.available_spots.append(self.available_spots(0))
                self.available_spots.remove(0)
        return random.choice(self.winning_spots)
        '''
    

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

