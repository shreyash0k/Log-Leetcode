class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        counter = 0 
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = True
                if j == i+1 and s[i]==s[j]:
                    dp[i][j] = True

                if j>i+1 and s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                
                if dp[i][j]:
                    counter+=1
        
        return counter

# tc O(n)^2 
# sc O(n)^2 since we are creating 2D dp 