class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))

            dp[(r, c)] = res
            return res

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))

        return longest
