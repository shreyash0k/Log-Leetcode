class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        hm = {i:0 for i in range(len(nums)+1)}

        for i in range(len(nums)):
            hm[nums[i]]+=1
        
        for key,value in hm.items():
            if value == 0:
                return key 
    

        # tc O(n)
        # sc O(n)