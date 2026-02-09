class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0            
            if amount in memo:
                return memo[amount]
            # check for each coin 
            min_coins = 1e9
            for coin in coins:
                if amount-coin>=0:
                    min_coins = min(min_coins, 1+ dfs(amount - coin))
            memo[amount] = min_coins
            return memo[amount]
        result = dfs(amount)
        return -1 if result == 1e9 else result

# tc 
# looping through coins going to take O(t) operation
# we are calling dfs function O(amount+1) times. 
# example amount = 9, coins [1,2,3]
# we we call dfs(9), dfs(8), dfs(7)... till dfs(0)
# so total tc = O(t*(n+1))

# sc 
# recursion stack can go O(amount+1)
# memoization will happen for O(amount+1) 
# total sc = O(amount+1)