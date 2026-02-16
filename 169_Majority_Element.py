class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       

        ''' boyer moore : 
        # go over list
        # if max frequency is 0 then pick current element
        # if current element is already picked up element, then increment max frequency else decrement maxfrequency. 
        # return picked up element. 
        '''
        pickedElement = 0 
        frequency = 0 
        for num in nums:
            if frequency == 0:
                pickedElement = num
            if num == pickedElement:
                frequency += 1
            else:
                frequency -= 1
        return pickedElement 

    

# tc O(n)
# sc O(1)