class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        # create 2d DP
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        # loop from end 
        max_length = 0
        startIndex = 0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if (i == j):
                    dp[i][j] = True
                elif (j==i+1 and s[i]==s[j]):
                    dp[i][j] = True
                elif(j>i+1 and s[i]==s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                
                if dp[i][j] and max_length<j-i+1:
                    max_length = j-i+1
                    startIndex = i

        return s[startIndex:startIndex+max_length]

        # maintain max_length and starting index
        # return string from starting index to max_length
        '''
        # for each character in string, 
        # set left and right to that position. 
        # check if characterAt left  == characterAt right, if yes make note of that substring. 
        # increment right pointer, decrement left pointer. check if palindrome, if yes keep doing this until they cross boundary. 

        

        max_length = 0
        start_index = 0 
        n = len(s)

        
        for i in range(n):
            left = right = i
            # odd case
            while left>=0 and right<n and s[left] == s[right]:
                if max_length<right-left+1:
                    start_index = left
                    max_length = right-left+1
                left-=1
                right+=1

            left,right=i,i+1
            while left>=0 and right<n and s[left] == s[right]:
                if max_length<right-left+1:
                    start_index = left
                    max_length = right-left+1
                left-=1
                right+=1
            
        
        return s[start_index:start_index+max_length]


# dp
# tc o(n)^2 for processing over 2D dp
# sc O(n)^2 for storing 2D dp

# two pointers
# tc O(n)^2 because for each character we are stretching it till n to check if it is longest palindrome
# sc O(1) 