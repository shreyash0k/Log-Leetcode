class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(substring, openParentheses, closeParentheses):
            if (openParentheses == n and closeParentheses == n):
                result.append("".join(substring))
                return
            
            if openParentheses < n:
                substring.append("(")
                dfs(substring, openParentheses+1, closeParentheses)
                substring.pop()

            if closeParentheses < openParentheses and closeParentheses < n:
                substring.append(")")
                dfs( substring, openParentheses, closeParentheses+1)
                substring.pop()
        
        dfs([],0,0)
        return result
    

# time complexity - 2 choices at 2n levels so 2^2n = 4 ^n 
# at each leaf node we can make copy. copy operation takes O(n) time.
# total time = (n*4^n)

# space complexity 
# Number of results ≈ 4^n (upper bound)
# Length of each = 2n = O(n)
# Total output space = O(n × 4^n)