class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        result = []

        def dfs(opening, closing, substr):
            if opening == n and closing == n :
                result.append(substr)
                return 
            if opening<n:
                dfs(opening+1, closing, substr+"(")
            if closing<n and opening>closing:
                dfs(opening,closing+1, substr+")")
                
        dfs(0,0,"")
        return result

    

# O(4^n)        
# O(n)
                            


        
        

    