class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # base case: full word matched
            if i == len(word):
                return True

            # out of bounds or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore neighbors
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            # backtrack
            board[r][c] = temp

            return found

        # try every cell as start
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# time complexity : O(m * n * 3^L) where m and n are dimensions of the board and L is the length of the word
# why 3^L? because from each cell we have at most 3 directions to explore for each character in the word

# space complexity : O(L) where L is the length of the word due to recursion stack
# space used for marking visited cells is O(1) since we are modifying the board in place
# overall space complexity is O(L)