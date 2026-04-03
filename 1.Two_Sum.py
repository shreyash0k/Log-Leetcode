class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmNums = {}
        for i,num in enumerate(nums):
            if target - num in hmNums:
                return [i,hmNums[target-num]]
            hmNums[num] = i
        
# tc O(n) because we are iterating through the list once
# sc O(n) because we are creating a new dictionary of size n