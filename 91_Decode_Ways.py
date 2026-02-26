class Solution:
    def numDecodings(self, s: str) -> int:
        memory = {len(s):1}
        def decode(i):
            if s[i] == "0":
                return 0 
            if i in memory:
                return memory[i]
            result = decode(i+1)
            if i+1<len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
               result = result +  decode(i+2)
            memory[i] = result
            return memory[i] 

        return decode(0)
        

# time complexity O(n) 
# space complexity O(n)