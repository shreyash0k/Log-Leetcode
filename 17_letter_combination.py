class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        result = []
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def dfs(index,subset):
            if index == len(digits):
                result.append("".join(subset))
                return
            
            letters =  mapping[digits[index]]
            for letter in letters:
                subset.append(letter)
                dfs(index+1,subset)
                subset.pop()

        dfs(0,[])
        return result 
    
# time complexity 
# each level we have 4 choices (worst case in case of digits 7 and 9)
# we might have n levels where n is length of digit
# so total leaf nodes = 4^n
# at each leaf node we copy subset to result. copy operation takes O(n) space.
# so multiplied by each node = (n*4^n)

# space complexity
# subset will have max o(4) space 
# result will have leaf nodes space. total leaf nodes are = 4^n 
# each leaf node will be of size n ["ad","ae","af"] 
# so total size will be n * 4 ^n
# recursion will use stack of size (n) 
# so total size becomes n * 4 ^ n 