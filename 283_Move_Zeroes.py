class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # maintain pointer1 that scans non zero elements 
        # maintain pointer2 that points to place for swap
        pointer1 = 0 
        pointer2 = 0 
      
        for pointer1 in range(0,len(nums)):
            if nums[pointer1] == 0:
                continue
            else:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer2+=1 
        
        return nums

# time complexity o(n)
# space complexity o(1)