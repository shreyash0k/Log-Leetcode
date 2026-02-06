from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clones = {}
        def dfs(node):
            if node in clones:
                return clones.get(node)

            clone = Node(node.val)
            clones[node] = clone
            clone.neighbors = [dfs(neighbor) for neighbor in node.neighbors]        

            return clone
        return dfs(node)

# time complexity = O(V+E)
# each vertex V is visited once 
# at each vertex we are iterating over edges 
# space complexity = O(V)
# in hashmap, key = original, value = copy 
# recursion stack is going to go max O(V)