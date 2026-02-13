class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create adj list 
        # perform dfs starting from "jfk" and return a list containing lexically sorted airports that can be visited 


        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for source, destination in tickets:
            adj[source].append(destination)
        
        result = []
        def dfs(source):
            while adj[source]:
                dfs(adj[source].pop())
            result.append(source)
        dfs("JFK")
        return result[::-1]

                

# tc O(E log E)
# sc O(E + V)