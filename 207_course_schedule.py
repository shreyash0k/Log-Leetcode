class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       
        processed = set()
        inProgress = set()
        courseMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        def dfs(course):
            if course in inProgress:
                return False
            if course in processed:
                return True 
            inProgress.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            
            inProgress.remove(course)
            processed.add(course)
            return True 

        for course in courseMap:
            if not dfs(course):
                return False
        
        return True 

# sc  O(V+E) O(E) to store graph, O(V) to create set, recursion stack. 
# tc O(V+E)
# O(E) to create hashmap. for each vertex we store its edges. 
# O(V+E) to process each vertex and visit its edges once so 