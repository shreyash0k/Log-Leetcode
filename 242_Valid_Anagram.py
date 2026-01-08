class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        solution = [0] * 26 
        if len(s)!=len(t):
            return False
        
        for i in s:
            solution[ord(i)-ord('a')] = solution[ord(i)-ord('a')] + 1 

        for i in t:
            solution[ord(i)-ord('a')] = solution[ord(i)-ord('a')] - 1 
        
        for i in solution:
            if i!=0:
                return False 

        return True 
        
# time complexity o(n)
# space complexity o(26)