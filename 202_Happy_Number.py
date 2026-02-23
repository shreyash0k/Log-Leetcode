class Solution:
    def isHappy(self, n: int) -> bool:
        # visti : 19, 82, 68, 100, 1 
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n ==1:
                return True
        return False 
        
    def sumOfSquares(self,n:int) -> int: 
        total = 0
        while n:
            digit = n%10
            total = total + digit**2
            n = n//10 
        return total 
                
# tc O(n)
# sc O(n)