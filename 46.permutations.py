class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
    
        def dfs(subset,used):
            if len(subset)==len(nums):
                result.append(subset.copy())
                return
        
            for i in range(0,len(nums)):
                if used[i] == True:
                    continue
                subset.append(nums[i])
                used[i] = True
                dfs(subset,used)
                subset.pop()
                used[i] = False            
        
        used = [False for _ in range(0,len(nums))]
        dfs([],used)
        return result 

# time complexity
# we have total n levels. at level 1 we make n choices, at level 2 we make n-1 choice,...
# so total n! choices 
# copying list to result list required o(n). this happens on each leafe node. total n! leaf nodes.
# O(n! * n) + O(n! * n)

# space complexity 
# recursion stack is of size n 
# permutation size is n 
# used array is of size n 
# result will have total n! elements. each of size n 
# so space complexity is O(n!*n)