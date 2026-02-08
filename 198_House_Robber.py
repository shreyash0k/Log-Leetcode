class Solution:
    def rob(self, nums: List[int]) -> int:
        total_house = len(nums)
        if total_house==1:
            return nums[0]
        memo = {}
        def dfs(position):
            if position>=total_house:
                return 0
            if position in memo:
                return memo[position]
            memo[position] = nums[position]+ max(dfs(position+2),dfs(position+3))
            return memo[position]
        return max(dfs(0),dfs(1))

# tc O(n) where n is total houses 
# sc O(n) we will store max robbery on each house + recursion stack will be O(n)