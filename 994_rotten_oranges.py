class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        fresh_oranges = 0 
        queue = deque()
        minutes = 0 
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col]==1):
                    fresh_oranges += 1
                elif(grid[row][col]==2):
                    queue.append((row,col))

        if fresh_oranges == 0:
            return 0 
            
        while queue:
            if fresh_oranges<=0:
                return minutes 
            
            for i in range(len(queue)):
                row,col = queue.popleft()
                for dr,dc in directions:
                    new_row = dr+row
                    new_col = dc+col
                    if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1):
                        grid[new_row][new_col] = 2 
                        queue.append((new_row,new_col))
                        fresh_oranges-=1
            
            minutes+=1
                
        return -1     

# time complexity: O(M*N) where M is number of rows and N is number of columns
# space complexity: O(M*N) in the worst case where all oranges are rotten and we have to store all of them in the queue