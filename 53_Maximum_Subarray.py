class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # go through list
        # keep adding element to sum and maintain maxsum
        # if at any point sum becomes less than 0, make it 0. 
        # return max sum so far


        maxSum = -1e9
        sum = 0
        for i in range(0,len(nums)):
            sum = sum + nums[i]
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0
        
        return maxSum

        # tc O(n)
        # sc O(1)