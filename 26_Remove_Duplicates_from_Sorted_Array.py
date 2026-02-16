class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        [0,0,1,1,1,2,2,3,3,4]
         l  temp                follower   number
         0  0                   0           0
         1  same as prev- 0     1           0
         2  different - 1       2           1
         3  same as prev        2           1
         4  same as prev 1      2           1
         5  different - 2       3           2
         6  same - 2            3           2
         7  different - 3       4           3
         8  same - 3            4           3
         9  different - 4       5           4 

        previous = nums[0]
        follower = 0  
        start from 1 
        if current element is same as previous then move to next number
        if current element is different than previous then set nums[follower] = nums[i]. increment follower. update previous. 


        ''' 
        if len(nums)==0:
            return 0 
        follower = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[follower] = nums[i]
                follower+=1
        
        return follower 
            
        # TC O(n)
        # SC O(1)