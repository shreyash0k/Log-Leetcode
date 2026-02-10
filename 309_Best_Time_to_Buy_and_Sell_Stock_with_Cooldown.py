class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can make 2 decisions at each level buy or cooldown. if we have already bought stocks then we can wither sell or cooldown 
        # if we ever sell, we have to do cooldown
        
        n = len(prices)
        memo = {}
        def dfs(buying,i):
            if i >= n:
                return 0
            if (buying,i) in memo:
                return memo[(buying,i)]
            if buying:
                buy = dfs(not buying,i+1) - prices[i]
                cooldown = dfs(buying,i+1)
                memo[buying,i] = max(buy,cooldown)
            else:
                sell = dfs(not buying,i+2) + prices[i]
                cooldown = dfs(buying,i+1)
                memo[buying,i] = max(sell,cooldown)
            
            return memo[buying,i]
    
        return dfs(True,0)

# tc 2(buy,sell) * n length of input prices  => O(n)
# sc O(n)