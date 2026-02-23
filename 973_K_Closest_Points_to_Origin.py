class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        distanceHeap = []
        for x,y in points:
            heapq.heappush(distanceHeap, ( -((x)**2 + (y)**2), [x,y]))
            if len(distanceHeap) > k: 
                heapq.heappop(distanceHeap)

        return [item for (_,item) in distanceHeap]
        
