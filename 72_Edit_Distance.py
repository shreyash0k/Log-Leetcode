class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # base if word1 is exausted that means we have to do some insertions.
        #      if word2 gets exausted that means we have some deletions to do 
        # if match, move on to i+1,j+1
        # if does not match, perform insert, delete, replace. move i and j
        
        memo = {}
        def dfs(i,j):    
            if i == len(word1):
                return (len(word2) - j )
            if j == len(word2):
                return (len(word1) - i )
            if (i,j) in memo:
                return memo[(i,j)]

            result = 0
            if word1[i]== word2[j]:
                result = result + dfs(i+1,j+1)
            else:
                result = result + 1 + min(dfs(i,j+1), dfs(i+1,j), dfs(i+1,j+1))
            
            memo[(i,j)] = result
            return result 

        return dfs(0,0)

# tc O(m*n)
# sc O(m*n)