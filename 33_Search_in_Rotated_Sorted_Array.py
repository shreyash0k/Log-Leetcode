class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check if mid is in left sorted portion or right sorted portion

            left = 0 
            right = len(nums)-1
            
            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] >= nums[left]:
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[left]:
                        left = mid + 1 
                    else:
                        right = mid - 1 
                else:
                    if target < nums[mid]:
                        right = mid - 1
                    elif target > nums[right]:
                        right = mid - 1
                    else:
                        left = left + 1                     
            return -1
       
       # tc O(log n)
       # sc O(1)