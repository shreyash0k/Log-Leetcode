class Solution:
    def maxArea(self, height: List[int]) -> int:
        # container area = width * height 
        # brute force approach is selecting first height and comparing it with all to find max area, then chosing next height and comparing it with remaining heights 
        # this will be O(n^2)
        # better approach is use two pointers 

        # assign pointer 1 to left. pointer 2 to right
        # check area
        # if pointer1's height is smaller increment that one
        # else decrement decrement pointer2 
        # once pointer1, pointer2 cross each other return max area found 

        left = 0 
        right = len(height) - 1 
        maxWater = 0
        while left<right:
            maxWater = max(maxWater, (right - left) * min(height[left],height[right]))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        
        return maxWater 

        # this approach uses O(n) time 
        # memory is O(1)