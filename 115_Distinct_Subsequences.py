class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # when t[i] == s[i] perfrom dfs(next letter S, next letter of T). Also try with next letter of S, same letter of T. Sum these 2.
        # when t[i] != s[i] perform dfs(next letter of S, same letter of T)

        def dfs(i,j):
            if j == len(t):
                return 1 
            if i == len(s):
                return 0
            
            result = 0
            if s[i] == t[j]:
                return (dfs(i+1,j+1) + dfs(i+1,j))
            else:
                return (dfs(i+1,j))

        return dfs(0,0)

# tc O(m*n)
# sc O(m*n)