class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # base case: full word matched
            if i == len(word):
                return True

            # out of bounds or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore neighbors
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            # backtrack
            board[r][c] = temp

            return found

        # try every cell as start
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# time complexity : O(m * n * 3^L) where m and n are dimensions of the board and L is the length of the word
# why 3^L? because from each cell we have at most 3 directions to explore for each character in the word

# space complexity : O(L) where L is the length of the word due to recursion stack
# space used for marking visited cells is O(1) since we are modifying the board in place
# overall space complexity is O(L)


# attempt using different style 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        def dfs(row,col,index):
            if index == len(word)-1:
                return True
                
            temp = board[row][col] 
            board[row][col] = "#"
            
            # explore 4 directions 
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            result = False
            for dc,dr in directions:
                new_row = row + dr
                new_col = col + dc 

                if 0<=new_row<rows and 0<=new_col<cols and board[new_row][new_col]==word[index+1]:
                    if dfs(new_row,new_col,index+1):
                        result = True
            
            board[row][col]= temp
            return result

        for i in range(rows):
            for j in range(cols):
                if word[0] == board[i][j]:
                    if dfs(i,j,0):
                        return True
        
        return False