class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxDP = [0] * n 
        minDP = [0] * n
        maxDP[0] = nums[0]
        minDP[0] = nums[0]

        for i in range(1,n):
            maxDP[i] = max(nums[i], nums[i] * maxDP[i-1], nums[i] * minDP[i-1])
            minDP[i] = min(nums[i], nums[i] * maxDP[i-1], nums[i] * minDP[i-1])
        
        return max(maxDP)
    
    # O(n)
    # O(n)