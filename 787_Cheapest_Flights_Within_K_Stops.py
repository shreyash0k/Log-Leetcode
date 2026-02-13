class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src] = 0 
        for i in range(0,k+1):
            temp = prices.copy()
            for source, destination, cost in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + cost < temp[destination]:
                    temp[destination] = prices[source] + cost
            
            prices = temp
        
        return -1 if prices[dst] == float("inf") else prices[dst]


# tc O(k*len(flights)) where k is total stops 
# sc O(n) where n is total nodes 