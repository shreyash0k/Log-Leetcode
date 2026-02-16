class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startList = sorted([start for start,end in intervals])
        endList = sorted([end for start,end in intervals])
        
        count = 0 
        rooms = 0 

        startPointer = 0
        endPointer = 0

        while startPointer < len(startList):
            if startList[startPointer]<endList[endPointer]:
                count = count + 1
                startPointer+=1
            else:
                count = count - 1 
                endPointer+=1
            rooms = max(rooms,count) 

        return rooms 

# tc O(n logn)
# sc O(n)