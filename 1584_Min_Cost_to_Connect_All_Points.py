class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adj list example point 0:[(1,4),(2,13),(3,8),(4,7)]
        n = len(points)
        adj = {i:[] for i in range(n)}

        # {0:[(1,2),(2,3),(3,5),(4,2)]}

        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                distance = abs(x1-x2)+abs(y1-y2)
                adj[i].append((distance,j))
                adj[j].append((distance,i))
        
        mHeap = [[0,0]] #distance, node
        minimumCost = 0 
        visited = set()
        while len(visited)<n:
            distance, node = heapq.heappop(mHeap)
            if node in visited:
                continue
            visited.add(node)
            minimumCost = distance + minimumCost
            for neighborDistance, neighbor in adj[node]:
                (neighbor not in visited) and heapq.heappush(mHeap, (neighborDistance, neighbor))
        
        return minimumCost
        # perform prmi's algorithm
        # start with point that is smallest weight, add it to heap 
        # select smallest from heap
        # make sure it is not visited.
        # add it to visited.
        # increment total length by adding current length
        # add its neighbors to heap


        # tc 
        # building adj list will take N^2 because of loops
        # heap can store N^2 values, since we are pushing all neigbhors for each vertex. so v^2
        # heap push and pop operation are O(logN)
        # total tc O(N^2 logN)

        # sc O(N^2)