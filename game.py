import math
import os
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self, x_player, o_player):
        #declares a 2D Array with whitespaces
        self.board = [['a'] * 4, ['b' ] * 3, ['c'] * 3]
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = None
        self.game_is_running = False
        
    def print_board(self):
        #this simply prints the board with its current values
        
        #clears the cmd or terminal
        os.system('cls')

        for r in range(0, len(self.board[0]) - 1):
            for c in range(0, 3):
                print((self.board[r][c]), end='')
                print(' | ', end='') if not c > 1 else None
            print('\n----------') if not r == (len(self.board[0]) - 2) else None

    #this method updates a spot on the 2D array game board with the current player's letter
    def update_spot(self, r_spot, c_spot):
        self.board[2][0] = self.current_player.letter

    #this method starts the game
    def start(self):
       self.current_player = self.x_player
       self.game_is_running = True
       self.runtime()

    #this is the runtime code of the game
    def runtime(self):
        while self.game_is_running:
            #get the current player's move
            print('Player', self.current_player.letter + ('\'s'), 'move: ')
            self.player_move = self.process_input(self.current_player.get_move())
            #self.update_spot(self.player_move.r_spot, self.player_move.c_spot)
            self.print_board()
            self.game_is_running = False
            break


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

    def __str__(self):
        return('[' + str(self.r_spot) + ', ' + str(self.c_spot) + "]")

game = TicTacToe(HumanPlayer('x'), ComputerPlayer('o'))
game.start()