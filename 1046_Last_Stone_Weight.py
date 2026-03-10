class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap)>1: 
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, -(y-x))
            
        return -heapq.heappop(maxHeap) if maxHeap else 0
    
    # tc O(n) to heapify, O(nlogn) to pop n elements 
    # sc O(n) to store elements 