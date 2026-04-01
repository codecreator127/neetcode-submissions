class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## if there is a directed cycle, then its impossible
        preMap = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()
        cycle = set()

        out = []


        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            out.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return out