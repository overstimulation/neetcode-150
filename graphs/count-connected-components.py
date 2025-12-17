from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        res = 0

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for neighbor in adj[i]:
                dfs(neighbor)

        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i)
        return res
