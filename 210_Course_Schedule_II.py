class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        complete, inProgress = set(), set()
        courseMap = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            courseMap[course].append(prerequisite)
        def dfs(course):
            if course in inProgress:
                return False
            if course in complete:
                return True
            inProgress.add(course)
            for prerequisite in courseMap[course]:
                if not dfs(prerequisite):
                    return False
            inProgress.remove(course)
            complete.add(course)
            result.append(course) 
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result 

# tc O(V+E) => processing hashmap requires O(E) (for each prereq)... processing dfs requires O(V+E)
# sc O(V+E) => storing hashmap requires O(V+E)