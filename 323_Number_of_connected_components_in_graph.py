class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        counter = 0 
        graph = {i:[] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
    
        for node in range(n):
            if node not in visited:
                counter+=1
                dfs(node)
        
        return counter

# TIME COMPLEXITY: O(V + E)
# - Building adjacency list: O(E) 
#   (iterate through all edges, add to both adjacency lists)
# - Outer for loop: iterates V times, but total DFS work is O(V + E)
#   - Each node visited exactly once: O(V)
#   - Each edge explored at most twice: O(E)
# - Total: O(V + E)

# SPACE COMPLEXITY: O(V + E)
# - Adjacency list: O(V + E)
#   (V keys in dict, total of 2E entries across all lists)
# - Visited set: O(V)
# - Recursion stack: O(V) worst case (linear graph)
# - Total: O(V + E)