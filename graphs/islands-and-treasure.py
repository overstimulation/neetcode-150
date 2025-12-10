import collections
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1
