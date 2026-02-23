class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) -1 
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >=goal:
                goal = i 
        
        if goal == 0:
            return True
        else:
            return False 
        
        #O(n) tc 
        #O(1) sc



        # start dfs from level 0 (current)
        # for i in range(len(nums[current]))
        # perform dfs and return true if any of them is true 
        # return False 
        '''
        cache = {}
        def jump(current):
            if current == len(nums)-1:
                return True 
            if current in cache:
                return cache[current]
            for i in range(0, nums[current]):
                if jump(current+i+1):
                    cache[current]  = True
                    return cache[current]  
            
            cache[current] = False
            return cache[current] 
        
        return jump(0)
        '''

        # dfs(0)
        #     dfs(1)
        #        dfs(2)
        #           dfs(3)
        #               dfs(4)
        # O(n^2) tc 
        # O(n^2) sc