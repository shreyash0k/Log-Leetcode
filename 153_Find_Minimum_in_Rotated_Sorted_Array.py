class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) -1 
        minimumElement = nums[0]

        while left <= right:
            if nums[left]<=nums[right]:
                return min(minimumElement,nums[left])
            mid = (left + right) // 2
            minimumElement = min(minimumElement, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1 
        
        return minimumElement

        # tc O(log n)
        # sc O(1)