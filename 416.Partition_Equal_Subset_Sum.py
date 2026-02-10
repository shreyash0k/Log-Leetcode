class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # check if sum % 2 == 0 
        # if it is an odd number return False
        # perform dfs starting from 0th position with remaining = sum/2 
            # if remaining = 0
                # you found a way return 1 
            # if remaining < 0 this is wrong way. return -1 or position ==n this is a wrong way.
            # take element or skip element
        
        total = sum(nums)
        if total%2 != 0:
            return False
        
        n = len(nums)
        memo = {}

        def dfs(position,remaining):
            if position ==n or remaining<0:
                return False
            if remaining == 0:
                return True
            if (position,remaining) in memo:
                return memo[(position,remaining)]
            
            memo[(position,remaining)] = (dfs(position+1,remaining - nums[position]) or dfs(position+1,remaining))
            return memo[(position,remaining)]

        return dfs(0,total/2)

# tc 
# we are visiting unique combinations of dfs(position,remaining) because of cache (memoization)
# position can go from 0 to n where n is number of elements in given input
# remaining can go from m to 0 where m is total/2
# so total tc is O(n*m)

# sc 
# O(n*m)
