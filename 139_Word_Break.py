class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

    # check each word in dictionary if it fits with s[0] till length of the word. if it fits then check next word from s[length of previous word +1] till length of the new word. If you reach len(s) that means there is fit. if you go out of bounds return 0 
        n = len(s)
        memo = {}
        def dfs(index):
            if index == n:
                return True

            if index in memo:
                return memo[index]
            
            for word in wordDict:
                if word == s[index:index+len(word)]:
                    if dfs(index+len(word)):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        return dfs(0)


# tc we are going over each word in dictionary => n * m where n is length of the dictionary and m is length of each word. We are doing this check on each index of original word 
# so total tc => n * m * k where k is length of original word

# sc in O(K) where k is length of original word 