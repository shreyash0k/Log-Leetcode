class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numberMap = Counter(nums)
        for number, frequency in numberMap.items():
            if frequency > 1:
                return True
        return False

# tc O(n) because we are iterating through the list once
# sc O(n) because we are creating a new dictionary of size n