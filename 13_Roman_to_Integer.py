class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        result = 0 
        for i in range(len(s)):
            if i+1<len(s) and roman_to_int_mapping[s[i]]<roman_to_int_mapping[s[i+1]]:
                result = result - roman_to_int_mapping[s[i]]
            else:
                result = result + roman_to_int_mapping[s[i]]
        return result

# tc - O(n)
# sc - O(1)