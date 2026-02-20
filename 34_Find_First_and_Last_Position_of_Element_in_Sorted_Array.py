class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(leftBias):
            left,right = 0,len(nums)-1
            idx = -1
            while left<=right:
                mid = (left + right ) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    idx = mid
                    if leftBias:
                        right = mid - 1 
                    else:
                        left = mid + 1 
            return idx

        left =  binarySearch(True)
        right = binarySearch(False)
        return [left,right]
        

        # continue perform binary search on left part after finding element to find first position
        # continue perform binary search on right part after finding element to find last position 
        # tc O(log n)+ O(log n)
        # sc O(1)class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(leftBias):
            left,right = 0,len(nums)-1
            idx = -1
            while left<=right:
                mid = (left + right ) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    idx = mid
                    if leftBias:
                        right = mid - 1 
                    else:
                        left = mid + 1 
            return idx

        left =  binarySearch(True)
        right = binarySearch(False)
        return [left,right]
        

        # continue perform binary search on left part after finding element to find first position
        # continue perform binary search on right part after finding element to find last position 
        # tc O(log n)+ O(log n)
        # sc O(1)