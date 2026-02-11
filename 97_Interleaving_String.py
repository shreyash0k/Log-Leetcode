class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        # start dfs from i = 0 and j =0 
        # i is a pointer for string 1.
        # j is a pointer for string 2 
        # if i+j == len(k) that means we found the solution return 1
        # if string1[i] == string2[j] and  == string3[i+j] then dfs(i+1,j) 
        # elif string3[i+j] == string1[i] then perfrom dfs(i+1,j)
        # elif string3[i+j] == string[j] then perform dfs(i,j+1)
        # else return 0 
        if len(s3)!= len(s1)+len(s2):
            return False
        memo = {}
        def dfs(i,j):
            if i+j == len(s3):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            result = False
            if i<len(s1) and s1[i] == s3[i+j]:
                result = result or dfs(i+1,j)
            if j<len(s2) and s2[j] == s3[i+j]:
                result = result or dfs(i,j+1)
            memo[(i,j)] = result
            return memo[(i,j)]
        return dfs(0,0) 

        # tc (m*n) where m is length of s1 and n is length of 2
        # sc O(m*n) for storing in memo + O(m+n) for recursion stack