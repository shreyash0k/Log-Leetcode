class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for number in nums:
            counts[number]+=1
        k=0
        for j in range(len(counts)):
            for i in range(counts[j]):
                nums[k] = j
                k+=1

# tc O(n) because we are iterating over the list once. 
# sc O(1) because we are using a fixed amount of space. 