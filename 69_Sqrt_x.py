class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        # start from 0 and check if square <= target
        # as soon as square crosses target stop and return the max number that you found 
        result = 0
        for i in range(x+1):
            if i**2 <= x:
                result = i
            else:
                break
        return result 

        ''' 
        # binary search solution 

        # calculate left, right, middle 
        # if middle square is greater than target, look in left part
        # if middle square is less than target, look in right part 
        # else return middle

        left = 0 
        right = x
        result = 0
        while left<=right:
            middle = (left + right) // 2
            if middle**2 < x:
                left = middle + 1
                result = middle
            elif middle**2 > x:
                right = middle - 1
            else:
                return middle
        
        return result 
