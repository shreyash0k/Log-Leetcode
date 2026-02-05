class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0 
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row,col):
            grid[row][col] = "0"
            queue = deque([(row,col)])
            directions = [(0,-1),(0,1),(-1,0),(1,0)]
            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    new_row = r+dr
                    new_col = c+dc
                    if (0<= new_row <rows and 0<= new_col<cols and grid[new_row][new_col]=="1"):
                        grid[new_row][new_col] = "0"
                        queue.append((new_row,new_col))  

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col]=="1"):
                    count+=1
                    bfs(row,col)

        return count                 
        # go through each cell of grid 
        # if cell = 1 increment count by 1  
        # run bfs / dfs to make all its adjacent lands as 0 
        #   bfs(row,col)
        #   
        # return count 


# time complexity 
# we are visiting each cell so m*n 
# while visiting first cell we might come across island made of full matrix so worst case m*n 
# total time complexity O(m+n) + O(m+n) = O(m+n)

# space complexity 
# we might have to store full matrix in queue. so worst case m*n


# dfs solution 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0 
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row,col):
            grid[row][col] = "0"
            directions = [(0,-1),(0,1),(-1,0),(1,0)]

            for dr, dc in directions:
                new_row = dr+row
                new_col = dc+col
                if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]=="1"):
                    dfs(new_row,new_col)
            

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col]=="1"):
                    count+=1
                    dfs(row,col)

        return count