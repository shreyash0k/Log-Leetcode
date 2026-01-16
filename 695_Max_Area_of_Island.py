class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_count = 0 
        rows = len(grid)
        cols = len(grid[0])
    
        def helper(r,c):
            # update max_count
            count = 0
            queue = deque()
            queue.append((r,c))
            grid[r][c] = 0
            while queue:
                row, col = queue.popleft()
                count+=1 
                # top
                if (row-1>=0 and grid[row-1][col]==1):
                    queue.append((row-1,col))
                    grid[row-1][col] = 0
                # bottom
                if (row+1<rows and grid[row+1][col]==1):
                    queue.append((row+1,col))
                    grid[row+1][col] = 0
                # left
                if (col-1>=0 and grid[row][col-1]==1):
                    queue.append((row,col-1))
                    grid[row][col-1] = 0
                # right
                if (col+1<cols and grid[row][col+1]==1):
                    queue.append((row,col+1))
                    grid[row][col+1] = 0
            
            return count
           

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1:
                    max_count = max(helper(i,j),max_count)

        return max_count
    

# why is time complexity O(M*N)?
# because we potentially visit every cell in the grid once
# but we are also adding this to queue and removing from queue then could you explain why it is still O(M*N)?
# each cell is processed a constant number of times (once when it is added to the queue and once when it is removed), so the overall time complexity remains O(M*N)
# space complexity: O(min(M,N)) in the worst case, the size of the queue
# how is space complexity O(min(M,N))?
# because in the worst case, the island could be very long and thin, leading to a queue that grows to the size of the smaller dimension of the grid
# for example, if the grid is 1xN or Mx1, the queue could grow to size N or M respectively 
