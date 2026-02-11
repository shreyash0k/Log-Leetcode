class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # perform dfs on each cell 
        # store results in cache 
        # return max from matrix 
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        def dfs(row,col,previous):
            if row==rows or row<0 or col == cols or col<0 or matrix[row][col]<=previous:
                return 0 
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            longest = 1 
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc 

                longest = max(longest, 1 + dfs(new_row,new_col,matrix[row][col]))

            memo[(row,col)] = longest
            return memo[(row,col)]

        longest = 1 
        for row in range(rows):
            for col in range(cols):
                longest = max(longest,dfs(row,col,-1))
        
        return longest
    
# tc O(m*n) because in first dfs itself we might cover all cells and later we won't have to visit them.
# sc O(m*n) because we are storing in memo and O(m*n) for max recursion stack