class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = set()
        
        def dfs(current_node, previous_node):
            if current_node in visited:
                return False
            
            visited.add(current_node)
            for neighbor in adj[current_node]:
                if neighbor == previous_node:
                    continue 
                if not dfs(neighbor, current_node):
                    return False
            
            return True 
                
        return (dfs(0,-1) and len(visited)==n)     

# tc O(O+E) visit each vertex and its edges once so O(V+E). 
# sc O(V+E) store adj list for vertex and edges 