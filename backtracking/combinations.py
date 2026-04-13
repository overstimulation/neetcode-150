class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def dfs(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n + 1):
                comb.append(i)
                dfs(i + 1, comb)
                comb.pop()

        dfs(1, [])
        return res
