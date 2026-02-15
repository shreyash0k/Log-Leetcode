class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = 0 
        left = 0 
        seen = set()
        for right in range(0,len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1 
            seen.add(s[right])
            maxSize = max(maxSize, right - left + 1 )
        
        return maxSize
    
# TC O(2N)
# SC O(N)