class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reachable[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                if reachable[i][k]:
                    for j in range(numCourses):
                        if reachable[k][j]:
                            reachable[i][j] = True

        return [reachable[u][v] for u, v in queries]
