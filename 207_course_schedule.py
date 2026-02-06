class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      
        courseMap = defaultdict(list)
        completed = set()
        inProgress = set()
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        
        def dfs(course):
            if course in inProgress:
                return False
            if course in completed:
                return True
            inProgress.add(course)
            for prerequisite in courseMap[course]:
                if not dfs(prerequisite):
                    return False
            inProgress.remove(course)
            completed.add(course)
            return True

        return all(dfs(course) for course in range(numCourses))
    
# sc  O(V+E) O(E) to store graph, O(V) to create set, recursion stack. 
# tc O(V+E)
# O(E) to create hashmap. for each vertex we store its edges. 
# O(V+E) to process each vertex and visit its edges once so 