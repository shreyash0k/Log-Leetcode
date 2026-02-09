class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {n:1}

        def dfs(pos):
            if pos in memo:
                return memo[pos]
            if s[pos] == "0":
                return 0
            
            result = dfs(pos+1)
            if pos+1<n:
                if s[pos] == "1":
                    result = result + dfs(pos+2)
                elif s[pos] == "2" and s[pos+1] in "0123456":
                    result = result + dfs(pos+2)
            memo[pos] = result
            return memo[pos] 
        return dfs(0)