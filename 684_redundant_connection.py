class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = {i:[] for i in range(1,len(edges)+1)}

         # 1:[2,3], 2:[1], 3:[1]
        def cycle(current,previous):
            if current in visited:
                return True
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor == previous:
                    continue
                if cycle(neighbor,current):
                        return True
            return False
   
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            visited = set()
            if cycle(node1,-1):
                return [node1,node2]
        
       
        
# tc - O(E*(V+E))
# sc - O(V+E)