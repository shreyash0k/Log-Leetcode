class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(row,col,d):
            result.append(matrix[row][col])
            visited.add((row,col))

            for i in range(4):
                nd = (d + i) %4
                dr, dc = directions[nd]
                new_row = dr + row
                new_col = dc + col 

                if (0<=new_row<rows and 0<=new_col<cols and (new_row,new_col) not in visited):
                    dfs(new_row,new_col,nd)
                    return
        dfs(0,0,0)
        return result

        # O(m*n) time
        # O(m*n) space 