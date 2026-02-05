class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        posDiagonal = set()
        negDiagonal = set()
        col = set()
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in col or r+c in posDiagonal or r-c in negDiagonal: 
                    continue

                col.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                board[r][c] = "."

        
        backtrack(0)
        return result 

# time complexity 
# we have n choice on row 1, n-3 choice row2, n-2 choices row3 and so on. 
# so we have n! choices 
# before and after recursion we perform add operation to sets. O(1)
# during copy we need O(n^2) time 
# so total time complexity = O(n! * n^2)
# n^2 is insignificant compared to n! so we will use say O(n!)

# space complexity O(n^2)