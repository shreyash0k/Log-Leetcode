class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left + right ) // 2 
            if (mid-1<0 or nums[mid]!=nums[mid-1]) and ((mid+1)==len(nums) or nums[mid]!=nums[mid+1]):
                return nums[mid]
            # either mid and mid-1 are equal 
            if nums[mid] == nums[mid-1]:
                pairStart = mid-1
            else:
                pairStart = mid
            
            if pairStart%2==0:
                left = mid +  1
            else:
                right = mid - 1

# tc O(log n)
# sc O(1)