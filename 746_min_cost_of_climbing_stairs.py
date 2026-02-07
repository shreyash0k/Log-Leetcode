class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        goal = len(cost)
        memo = {}
        def dfs(position):
            if (position>=goal):
                return 0
            if position in memo:
                return memo[position]
            memo[position] = cost[position] + min(dfs(position+1),dfs(position+2))
            return memo[position]
        return min (dfs(0),dfs(1))     

# tc O(n)
# sc O(n)