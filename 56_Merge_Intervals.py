class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort intervals 
        # create a result list
        # add first element to this result list
        # compare 1th element in original list with 0th element in result list.
        # if overlap, combine
        # else append current element 


        #[[1,3],[2,6],[8,10],[15,18]]

        # intervals [[1,3], ]
        
        if len(intervals)==1:
            return [intervals[0]]
        intervals.sort(key=lambda x:x[0])
        result = []
        result.append(intervals[0])  # check if it will be append or add.
        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])
        return result

        # tc O(n logn)
        # sc O(n)