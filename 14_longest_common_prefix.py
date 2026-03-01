class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        for i in range(0,len(strs[0])):
            for string in strs:
                if len(string)<=i or string[i]!=strs[0][i]:
                    return strs[0][:i] 
                
        return strs[0]
    
# tc O(m*n) where m i number of string and n is max lenght of any string 
# sc is O(m^2) 