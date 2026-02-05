class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0 
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = 0 
            directions = [(0,-1),(0,1),(-1,0),(1,0)]
            area = 1 
            while queue:
                row,col = queue.popleft()
                for dr,dc in directions:
                    new_row = dr + row
                    new_col = dc + col 
                    if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1):
                        grid[new_row][new_col] = 0 
                        area = area+1 
                        queue.append((new_row,new_col))
            return area
                

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col]==1):
                    max_area = max(max_area,bfs(row,col))

        return max_area 

# time complexity = O(m*n) + O(m*n)
# space complexity = o(m*n)