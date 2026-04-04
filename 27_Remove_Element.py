class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valPointer = len(nums)-1
        countVal = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums[i],nums[valPointer] = nums[valPointer], nums[i]
                countVal+=1
                valPointer-=1    
        return len(nums) - countVal

# tc O(n) because we are iterating through the list once
# sc O(1) because we are not using any extra space