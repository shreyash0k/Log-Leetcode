class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0]*26

        for char in s:
            letters[ord(char) - ord('a')]+=1
        
        for char in t:
            letters[ord(char)- ord('a')]-=1
        
        for val in letters:
            if val!=0:
                return False
        
        return True

# tc O(n) because we are iterating through the strings once. O(3n) = O(n)
# sc O(26) because we are creating a new list of size 26