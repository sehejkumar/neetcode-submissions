class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqMap[course].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereqMap[course] == []:
                return True
            visited.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            prereqMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True