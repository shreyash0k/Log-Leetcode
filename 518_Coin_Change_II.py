class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(sum,i):
            if sum>amount:
                return 0 
            
            if sum == amount:
                return 1
            
            if i == len(coins):
                return 0
                
            if (sum,i) in memo: 
                return memo[(sum,i)]

            memo[(sum,i)] = dfs(sum+coins[i],i) + dfs(sum,i+1)
            return memo[(sum,i)]

        return dfs(0,0)
    
# tc 
# at each node we are performing O(1) operation
# there are total (target * total coins) states 
# tc => O(t*n)

# sc => O(t*n)