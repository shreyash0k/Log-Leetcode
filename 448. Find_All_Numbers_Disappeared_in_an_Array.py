class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[ abs(nums[i])-1 ] = - abs(nums[ abs(nums[i])-1 ])
        result = []
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        return result
    
    # tc O(n)
    # sc O(1) if we don't count result array