class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        p = 0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    p += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        p -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        p -= 2
        return p
