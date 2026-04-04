class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for string in strs:
            asci = [0]*26
            for char in string:
                asci[ord(char)-ord('a')]+=1
            hm[tuple(asci)].append(string)
        return list(hm.values())


# tc O(n*m) because we are iterating through the list of strings and the length of the strings
# sc O(n*m) because we are creating a new dictionary of size n*m