class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        # DFS with memo — try matching characters at positions i, j
        # 
        # Base: i or j out of bounds -> 0
        # Match:    text1[i] == text2[j] -> 1 + dfs(i+1, j+1)
        # No match: max(dfs(i+1, j), dfs(i, j+1))
        #
        # Time: O(m*n)  Space: O(m*n)
        
        m = len(text1)
        n = len(text2)
        memo = {}
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1,j+1)
            else:
                memo[(i,j)] = max(dfs(i+1,j),dfs(i,j+1))
            return memo[(i,j)]

        return dfs(0,0)