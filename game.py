import math

class TicTacToe:
    def __init__(self, x_player, o_player):
        #declares a 2D Array with whitespaces
        self.board = [[' ' * 3], [' ' * 3], [' ' * 3]]
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = None
        
    def print_board(self):
        #this simply prints the board with its current values
        
        #the first part is to only print -- if it is not the first row
        first = True
        for r in self.board:
            print('-- ' * 4) if not first else None
            first = False
            for c in r:
                print('| '.join(c).join(' |'))

    def update_spot(self, r_spot, c_spot, ):
        self.board[r_spot][c_spot] = "f"

game = TicTacToe()
game.print_board()