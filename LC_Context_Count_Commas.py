class Solution:
    def countCommas(self, n: int) -> int:
        result = 0 
        threshold = 999 
        multiplier = 1 
        while n>threshold:
            result = result + (n - threshold)* multiplier
            threshold = threshold * 1001 
            multiplier+=1 
        return result 

       
        
