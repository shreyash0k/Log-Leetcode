class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n= len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        def dfs(node, end):
            if node > end:
                return 0
            if node in memo:
                return memo[node]
            memo[node] = max(nums[node]+dfs(node+2,end),dfs(node+1,end))
            return memo[node]
        
        result1 = dfs(0,n-2)
        memo = {}
        result2 = dfs(1,n-1)
        return max(result1,result2)

# tc O(n-1) + O(n-1)=> O(n)
# sc O(n-1) => O(n)