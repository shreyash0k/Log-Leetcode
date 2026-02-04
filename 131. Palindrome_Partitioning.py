class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def dfs(index,subset):
            if index == len(s):
                result.append(subset.copy())
                return
            
            for i in range(index,len(s)):
                if self.isPalindrome(s,index,i):
                    subset.append(s[index:i+1])
                    dfs(i+1,subset)
                    subset.pop()
                
        dfs(0,[])
        return result 
        
    def isPalindrome(self,s,left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    

# time complexity 
# we have n-1 gaps in given word 
# each gap has 2 choices. cut or not cut
# 2^(n-1)
# copying requires O(n) time complexity
# total time complexity = O(n* 2^(n-1))

# space complexity 
# O(n × 2^n)