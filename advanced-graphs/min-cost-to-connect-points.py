import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        visited = set()
        min_heap = [(0, 0)]
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)

            if i in visited:
                continue

            total_cost += cost
            visited.add(i)

            x1, y1 = points[i]

            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, j))

        return total_cost
