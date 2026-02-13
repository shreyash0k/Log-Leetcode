class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # use dijkstra's algorithm
        maxHeight = 0 
        mHeap = [[grid[0][0],0,0]]
        processed = set((0,0))
        n = len(grid)
        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        while mHeap:
            currentHeight, row, col = heapq.heappop(mHeap)  # 0,0,0
            if row == n-1 and col == n-1:
                return currentHeight

            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col 
                if (0<=new_row<n and 0<=new_col<n and (new_row,new_col) not in processed):
                    heapq.heappush(mHeap,(max(currentHeight,grid[new_row][new_col]), new_row, new_col))
                    processed.add((new_row,new_col))

# tc O(n^2 * log N)
# sc O(n^2)