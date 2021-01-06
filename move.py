
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