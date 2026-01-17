class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = 0 
        rows = len(grid)
        cols = len(grid[0])

        rottenQueue = deque() 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    rottenQueue.append((i,j))
        
        if freshOranges == 0:
            return 0

        totalTime = 0 
        while rottenQueue and freshOranges >0:
            size = len(rottenQueue)
            for _ in range(size):
                r,c = rottenQueue.popleft() 
                if c-1>=0 and grid[r][c-1] == 1:
                    freshOranges-=1
                    rottenQueue.append((r,c-1))
                    grid[r][c-1] = 2
                
                if c+1<cols and grid[r][c+1] == 1:
                    freshOranges-=1 
                    rottenQueue.append((r,c+1))
                    grid[r][c+1] = 2 

                if r-1>=0 and grid[r-1][c] == 1:
                    freshOranges-=1 
                    rottenQueue.append((r-1,c))
                    grid[r-1][c] = 2 

                if r+1<rows and grid[r+1][c] == 1:
                    freshOranges-=1 
                    rottenQueue.append((r+1,c))
                    grid[r+1][c] = 2 
            totalTime+=1 
        
        if freshOranges > 0:
            return -1
        
        return totalTime 
                

# time complexity: O(M*N) where M is number of rows and N is number of columns
# space complexity: O(M*N) in the worst case where all oranges are rotten and we have to store all of them in the queue