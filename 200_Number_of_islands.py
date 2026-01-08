class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # calculate rows cols count and numberOfIslands 
        rows = len(grid)
        cols = len(grid[0])
        numOfIsland = 0 

        def findIsland(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] = '0'
            while queue:
                row,col = queue.popleft()
                # visit left 
                if (row-1>=0 and grid[row-1][col] =='1'):
                    grid[row-1][col] = '0'
                    queue.append((row-1,col))

                # visit right
                if (row+1<rows and grid[row+1][col]=='1'):
                    grid[row+1][col] = '0'
                    queue.append((row+1,col))

                # visit bottom 
                if (col+1<cols and grid[row][col+1] == '1'):
                    grid[row][col+1] = '0'    
                    queue.append((row,col+1))
            
                # visit top 
                if (col-1>=0 and grid[row][col-1] == '1'):
                    grid[row][col-1] = '0'      
                    queue.append((row,col-1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    findIsland(row,col)
                    numOfIsland+=1 
        
        return numOfIsland 

# time complexity - o(row * col)
# space complexity - o(row * col)