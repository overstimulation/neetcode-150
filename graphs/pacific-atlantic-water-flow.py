from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set, prev_height):
            if (r, c) in reachable_set or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prev_height:
                return
            reachable_set.add((r, c))

            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, 0)
            dfs(r, COLS - 1, atlantic_reachable, 0)

        for c in range(COLS):
            dfs(0, c, pacific_reachable, 0)
            dfs(ROWS - 1, c, atlantic_reachable, 0)

        return list(pacific_reachable.intersection(atlantic_reachable))
