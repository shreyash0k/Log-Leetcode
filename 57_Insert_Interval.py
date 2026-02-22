class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

      # go over list one interval at a time
        # if newInterval starts before current item, 
                # append newInterval to result,
                # append rest of list to result 
                # return result 
        # else if newInterval starts after current item,
                # current item is safe, append that to list.
                # we might have more collisions in future so keep going 
        #  else (there is overlapping)
                # update new interval 
        
        # append new interval
        # return result 
        # [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [3,8]
        # [1,2],
        result = []
        for i in range(0,len(intervals)):
            if newInterval[1]<intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result 
            elif newInterval[0]>intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [ min(newInterval[0], intervals[i][0] ) ,  max(newInterval[1], intervals[i][1] )]

        result.append(newInterval)
        return result         

        # O(n)
        # O(n)