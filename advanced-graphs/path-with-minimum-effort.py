import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        R, C = len(heights), len(heights[0])
        min_effort = {(r, c): float("inf") for r in range(R) for c in range(C)}
        min_effort[(0, 0)] = 0
        pq = [(0, 0, 0)]

        while pq:
            effort, r, c = heapq.heappop(pq)

            if r == R - 1 and c == C - 1:
                return effort

            if effort > min_effort[(r, c)]:
                continue

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < min_effort[(nr, nc)]:
                        min_effort[(nr, nc)] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
        return 0
