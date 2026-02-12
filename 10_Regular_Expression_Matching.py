class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        # Top-down DP with memoization
        # i = pointer for string s, j = pointer for pattern p
        #
        # At each state (i, j):
        #   1. If '*' follows current pattern char (j+1 < len(p) and p[j+1] == '*'):
        #      - Use '*' (match 0 occurrences): skip pattern pair → dfs(i, j+2)
        #      - Use '*' (match 1+ occurrences): if current chars match → dfs(i+1, j)
        #   2. Else if current chars match (exact or '.'): advance both → dfs(i+1, j+1)
        #   3. Else: no match → return False
        #
        # Base cases:
        #   - Both pointers exhausted (i >= len(s) and j >= len(p)) → True
        #   - Pattern exhausted but string remains (j >= len(p)) → False
        #   - String exhausted but pattern remains → handled by '*' consuming 0 matches
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            
            match = i<len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1<len(p) and p[j+1] == "*":
                memo[(i,j)] = ((match and dfs(i+1,j)) or dfs(i,j+2))
                return  memo[(i,j)]
            if match:
                memo[(i,j)] = (dfs(i+1,j+1))
                return memo[(i,j)]
            memo[(i,j)] = False
            return memo[(i,j)]
        
        return dfs(0,0)

'''
TC: O(m × n) — where m = len(s) and n = len(p). Each (i, j) state is computed at most once due to memoization.
SC: O(m × n) — for the memo dictionary and recursion stack.
'''