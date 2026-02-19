class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left,right):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1 
                right-=1
        size = len(nums)
        k = k % size
        reverse(0,size-1)
        reverse(0,k-1)
        reverse(k,size-1)
        
    
        # tc O(n)
        # sc O(1)
       
        

