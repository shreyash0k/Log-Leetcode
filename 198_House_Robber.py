class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(i):
            if i>=len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            rob_current = nums[i] + helper(i+2)
            
            skip_current = helper(i+1)

            memo[i] = max(rob_current,skip_current)

            return memo[i]
        
        return helper(0)

# time complexity - o(n) 
# space complexity - o(n)