class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        heapq.heapify(nums)
        result = []
        for num in nums:
            result.append(heapq.heappop(nums))
        return result

# O n log n 