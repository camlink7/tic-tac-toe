import math
import os
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self, x_player, o_player):
        #declares a 2D Array with whitespaces
        self.board = [[' ' for i in range(50)] for j in range(50)]
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = None
        self.game_is_running = False
        self.needs_cleared = False
        self.move_successful = False
        self.game_winner = None
        
    #this simply prints the board with its current values
    def print_board(self, clear):
        #notes if board is going to be cleared on not
        self.temp_clear = clear
        
        #clears the cmd or terminal
        os.system('cls') if clear else None
        self.needs_cleared = False

        #this will set the board to need to be cleared in the future because it was not cleared on this print
        self.needs_cleared = True if not self.temp_clear else None

        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[0])):
                print((' ' + self.board[r][c]), end='') 
                print('  | ', end='') if not c == len(self.board[0]) - 1 else None
            print('\n' + ('-----' * len(self.board[0])) + '--') if not r == (len(self.board) - 1) else None
        print('')

    #this method updates a spot on the 2D array game board with the current player's letter
    def update_spot(self, r_spot, c_spot):
        if self.board[r_spot][c_spot] == ' ':
            self.board[r_spot][c_spot] = self.current_player.letter
            self.print_board(True)
            self.move_successful = True
            self.check_for_winner()
        else:
            os.system('cls')
            print("That spot is already taken!\n")
            self.print_board(False)

    #this method checks for a winner of the game
    def check_for_winner(self):
        #ensures board isnt full before checking for winner
        if not self.check_for_full_board():
            #check for 3 in a row for each row
            output = ''
            for r in range(0, len(self.board)):
                for c in range(0, len(self.board[0])):
                    output += self.board[r][c]
                if output == 'x' * len(self.board[0]):
                    self.game_winner = self.x_player
                    self.end('Player X has won!')
                    return True
                elif output == 'o' * len(self.board[0]):
                    self.game_winner = self.o_player
                    self.end('Player O has won!')
                    return True
                output = ''
            
            #check for 3 in a column for each column
            output = ''
            for c in range(0, len(self.board[0])):
                for r in range(0, len(self.board)):
                    output += self.board[r][c]
                if output == 'x' * len(self.board):
                    self.game_winner = self.x_player
                    self.end('Player X has won!')
                    return True
                elif output == 'o' * len(self.board):
                    self.game_winner = self.o_player
                    self.end('Player O has won!')
                    return True
                output = ''
                
            #checks for 3 in a diagonal from left to right
            
                
        else:
            #ends game, prints tie, and returns True is the game board is full
            self.end("Tie!")
            return True

    #this method checks to see if the game board is full
    def check_for_full_board(self):
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[0])):
                if self.board[r][c] == ' ':
                    return False
        return True

    #this method starts the game
    def start(self):
       self.current_player = self.x_player
       self.game_is_running = True
       self.runtime()

    #this method ends the game and prints a message out 
    def end(self, msg):
        os.system('cls')
        print(msg + '\n')
        self.print_board(False)
        self.game_is_running = False
        input('\n\nPress enter key to close...')


    #this is the runtime code of the game
    def runtime(self):
        self.print_board(True)
        while self.game_is_running:
            #set move_successful to false
            self.move_successful = False
            #get the current player's move
            print('\n\nPlayer', self.current_player.letter + ('\'s'), 'move: ', end='')
            self.player_move = self.process_input(self.current_player.get_move())
            if self.player_move.valid:
                self.update_spot(self.player_move.r_spot, self.player_move.c_spot)
            else:
                self.print_board(False)

            #check to see if the game needs ended
            if not self.game_is_running:
                break

            #go to the opposite player for their turn only if the move was successful
            if self.move_successful:
                if self.current_player.letter == 'x':
                    self.current_player = self.o_player
                else:
                    self.current_player = self.x_player


    #this processes a players input and calls the correct methods if it can understand the input
    def process_input(self, p_input):
        try:
            return Move(int((p_input.strip().split(','))[0]), int((p_input.strip().split(','))[1]), self.current_player, True, self.board)
        except:
            p_move = Move(5, 5, self.current_player, False, self.board)
            if not p_move.valid:
                os.system('cls')
                print("Unknown input! Please try again!\n")
            return p_move



#This is class for a move on the board
class Move():
    def __init__(self, r_spot, c_spot, player, valid, board):
        self.r_spot = r_spot
        self.c_spot = c_spot
        self.player = player
        self.board = board
        self.valid = valid
        self.valid = self.check_valid() if self.valid else None

    def __str__(self):
        #updated the __str__ to easily print the move
        return('[' + str(self.r_spot) + ', ' + str(self.c_spot) + "]")

    #This ensures the move is within the boundaries of the board. If it isn't it warns the player
    def check_valid(self):
        if self.r_spot >= 0 and self.r_spot < len(self.board) and self.c_spot >= 0 and self.c_spot < len(self.board[0]):
            return True
        elif self.r_spot < 0 or self.r_spot >= len(self.board) or self.c_spot < 0 or self.c_spot >= len(self.board[0]):
            os.system('cls')
            print("That spot doesn't exist\n")
        return False

game = TicTacToe(HumanPlayer('x'), HumanPlayer('o'))
game.start()