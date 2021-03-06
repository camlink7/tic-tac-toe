import math
import os
from player import HumanPlayer, ComputerPlayer
from move import Move

class TicTacToe:
    def __init__(self, x_player, o_player, col, row):
        #declares a 2D list with whitespaces
        self.board = [[' ' for i in range(col)] for j in range(row)]
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = None
        self.game_is_running = False
        self.needs_cleared = False
        self.move_successful = False
        self.game_winner = None
        self.ai_score = 0

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
                print(' |', end='') if not c == len(self.board[0]) - 1 else None
            print('\n' + ('----' * len(self.board[0]))) if not r == (len(self.board) - 1) else None
        print('')

    #this method updates a spot on the 2D list game board with the current player's letter
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
                
            #checks for 3 in a diagonal from left to right if the board is evenly squared and not oblong
            if len(self.board) == len(self.board[0]):
                output = ''
                length = len(self.board)
                for r in range(0, length):
                    output += self.board[r][r]
                    if output == 'x' * length:
                        self.game_winner = self.x_player
                        self.end('Player X has won!')
                        return True
                    elif output == 'o' * length:
                        self.game_winner = self.o_player
                        self.end('Player O has won!')
                        return True

            #checks for 3 in a diagonal from right to left if the board is evenly squared and not oblong
            if len(self.board) == len(self.board[0]):
                output = ''
                length = len(self.board)
                count = length - 1
                for r in range(0, length):
                    output += self.board[r][count]
                    count -= 1
                    if output == 'x' * length:
                        self.game_winner = self.x_player
                        self.end('Player X has won!')
                        return True
                    elif output == 'o' * length:
                        self.game_winner = self.o_player
                        self.end('Player O has won!')
                        return True
                
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

    #this method will get an return a list of strings that are the available spots that can be played
    def get_available_spots(self):
        output = []
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[0])):
                if self.board[r][c] == ' ':
                    output.append(str(r) + ',' + str(c))
        return output



    #this method starts the game
    def start(self):
        self.tutorial()
        self.x_player.set_game(self)
        self.o_player.set_game(self)
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

    #this method prints and runs the code for a simple tutorial of the game
    def tutorial(self):
        os.system('cls')
        print('Welcome to Tic Tac Toe!\n-----------------------------\nTo choose a spot, simply put the coordinates in and seperate them with a comma\nExample: 0,0' +
        '\nThis would pick the top left spot\n\nPress enter to start the game!')
        input('')


    #this is the runtime code of the game
    def runtime(self):
        self.print_board(True)
        while self.game_is_running:
            #set move_successful to false
            self.move_successful = False
            #get the current player's move
            print('\n\nPlayer ' + self.current_player.letter + ('\'s ') + 'move: ', end='')
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

game = TicTacToe(HumanPlayer('x'), ComputerPlayer('o'), 3, 3)
game.start()