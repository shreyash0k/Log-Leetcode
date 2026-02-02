class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # store all the subsets 
        result = [] 
        def helper(index,subset):
            # break condition 
            if (index == len(nums)):
                result.append(subset.copy())
                return
            
            #include current item 
            subset.append(nums[index])
            helper(index+1,subset)

            subset.pop()
            helper(index+1,subset)

        helper(0,[])
        return result 

# 2 choices per number 
# n(2 ^n) choices 

# space 2 ^ n 