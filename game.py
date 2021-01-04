import math

class TicTacToe:
    def __init__(self):
        #declares a 2D Array with whitespaces
        self.board = [[' ' * 3], [' ' * 3], [' ' * 3]]
        
    def print_board(self):
        first = True
        for r in self.board:
            print('-- ' * 4) if not first else None
            first = False
            for c in r:
                print('| '.join(c).join(' |'))


game = TicTacToe()
game.print_board()