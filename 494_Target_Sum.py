class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # dfs 
             # base case
             # if target reached return 1 
             # if beyond target, return 0 
             # return sum of ways between taking the next number as + and taking the next number as - 
        memo = {}
        def dfs(total,position):
            if position == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (total,position) in memo:
                return memo[(total,position)]

            memo[(total,position)] = dfs(total+nums[position],position+1) + dfs(total-nums[position],position+1)
            return memo[(total,position)]

        return dfs(0,0)

# tc we will get combinations of total,position
# total can range from -sum(elements) to + sum(elements) => 2S 
# position can range from 0 to N => N+1 
# tc => (N+1)(2S + 1)
# N*S
# same for space complexity