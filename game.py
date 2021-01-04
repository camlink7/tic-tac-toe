import math
import os
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self, x_player, o_player):
        #declares a 2D Array with whitespaces
        self.board = [[' ' * 3], [' ' * 3], [' ' * 3]]
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = None
        self.game_is_running = False
        
    def print_board(self):
        #this simply prints the board with its current values
        
        #clears the cmd or terminal
        os.system('cls')
        #the first part is to only print -- if it is not the first row
        first = True
        first2 = True
        for r in self.board:
            print('-- ' * 4) if not first else None
            first = False
            for c in r:
                print('| '.join(c).join(' |')) if not first2 else None
                first2 = False

    #this method updates a spot on the 2D array game board with the current player's letter
    def update_spot(self, r_spot, c_spot):
        self.board[r_spot][c_spot] = self.current_player.letter

    #this method starts the game
    def start(self):
       self.current_player = self.x_player
       self.game_is_running = True
       self.runtime()

    #this is the runtime code of the game
    def runtime(self):
        while self.game_is_running:
            #get the current player's move
            print('Player', self.current_player.letter.join('\'s'), 'move: ')
            self.player_move = self.process_input(self.current_player.get_move())
            self.update_spot(self.player_move.r_spot, self.player_move.c_spot)


    #this processes a players input and calls the correct methods if it can understand the input
    def process_input(self, p_input):
        try:
            return Move(int((p_input.strip().split(','))[0]), int((p_input.strip().split(','))[1]), self.current_player)
        except:
            print("\nUnknown input! Please try again!\n")
            return None



class Move():
    def __init__(self, r_spot, c_spot, player):
        self.r_spot = r_spot
        self.c_spot = c_spot
        self.player = player

game = TicTacToe(HumanPlayer('x'), ComputerPlayer('o'))
game.start()