class TicTacToe:

    def __init__(self, n: int):
        self.row = [0]*n
        self.col = [0]*n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n 

    def move(self, row: int, col: int, player: int) -> int:
        delta = 1 if player == 1 else -1 
        self.row[row]+=delta
        self.col[col]+=delta
        if (row==col):
            self.diagonal +=delta
        if (row+col==self.n-1):
            self.anti_diagonal +=delta
        
        
        if self.row[row] == self.n or self.col[col] == self.n or self.diagonal == self.n or self.anti_diagonal == self.n : 
            return player
        elif self.row[row] == -self.n or self.col[col] == -self.n or self.diagonal == -self.n or self.anti_diagonal == -self.n :
            return player
        else: 
            return 0 

# time complexity: O(1) for each move
# space complexity: O(n) for storing row and column counts