class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for number in num_set:
            if number - 1 not in num_set:
                length = 1 
                current = number
                while current + 1 in num_set:
                    length = length + 1 
                    current = current + 1 
                longest = max(longest, length)
        return longest
    
# TC O(n)
# SC O(n)