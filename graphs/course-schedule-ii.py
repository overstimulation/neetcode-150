import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        in_degree = {c: 0 for c in range(numCourses)}

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        queue = collections.deque([c for c in in_degree if in_degree[c] == 0])

        result = []

        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) == numCourses:
            return result
        else:
            return []
