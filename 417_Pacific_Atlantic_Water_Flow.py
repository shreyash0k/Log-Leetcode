class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(row,col,ocean):   
            if (row,col) in ocean :
                return
            ocean.add((row,col))     
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc 
                if (0<=new_row<rows and 0<=new_col<cols and heights[new_row][new_col]>=heights[row][col]):
                    dfs(new_row,new_col,ocean)
        
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)

        return list(map(list,pacific & atlantic))

        
# tc - our first dfs might cover all cells so m*n 
# in next iterations it will be skipped 
# at last we are taking itersection between two lists o(lenght of min of 2 sets)
# so total tc O(m*n)
# sc - O(m*n) + O(m*n) 