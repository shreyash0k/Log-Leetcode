class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        

        # go through all cell
        # if current cell is gate, perform bfs on that cell 
        

        # bfs 
        # add current element to queue 
        # while queue is not empty 
        # pop element from queue 
        # add its neighbors to queue with value as current counter
        # every time we pop from queue we increment counter by 1 


        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque()
        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        for row in range(rows):
            for col in range(cols):
                if (rooms[row][col] == 0):
                    queue.append((row,col))

        while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    new_row = dr+ r
                    new_col = dc + c
                    if(0<=new_row<rows and 0<=new_col<cols and rooms[new_row][new_col]==2147483647):
                        rooms[new_row][new_col] = rooms[r][c]+1
                        queue.append((new_row,new_col))
        
        
# time complexity = O(m*n)
# space compexity = O(m*n)