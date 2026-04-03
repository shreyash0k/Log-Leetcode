class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

# tc O(2n) because we are creating a new list of size 2n
# sc O(2n) because we are creating a new list of size 2n