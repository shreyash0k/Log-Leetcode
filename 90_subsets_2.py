class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def helper(i, subset):
            if i == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            helper(i+1,subset)
    
            subset.pop()
            while i+1 < len(nums) and nums[i+1]==nums[i]:
                i = i + 1 
            helper(i+1,subset) 

        helper(0,[])
        return result 


# time complexity 
# sorting will need nlog(n)
# we have 2 choices at each element -> 2 * 2 * 2 * 2 -> 2^n
# where n is length of the list. 
# we are going to call copy() function 2^n times. each call to copy() needs o(n) time
# so total time complexity is O(n logn) + O(n * 2^n)
 

# space complexity
# recursion stack can go max n because of our base condition 
# we can have total 2^n subsets and each subset can be of length n 
# so total space needed is n * 2^n 
