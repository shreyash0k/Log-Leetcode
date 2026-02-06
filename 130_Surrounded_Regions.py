class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        rows, cols = len(board), len(board[0])
        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        def bfs(row,col):
            if (board[row][col]!="O"):
                return

            queue = deque()
            queue.append((row,col))
            board[row][col] = "1"

            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc 
                    if (0<=new_row<rows and 0<=new_col<cols and board[new_row][new_col]=="O"):
                        board[new_row][new_col] = "1"
                        queue.append((new_row,new_col))

        for c in range(cols):
            bfs(0,c)
            bfs(rows-1,c)
        
        for r in range(rows):
            bfs(r,0)
            bfs(r,cols-1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=="1":
                    board[row][col] = "O"
                else: 
                    board[row][col]= "X"

# tc - O(m*n) + O(m*n)
# sc - O(m*n)