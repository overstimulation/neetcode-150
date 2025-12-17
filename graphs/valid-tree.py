from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for j in adj[i]:
                dfs(j)

        dfs(0)
        return len(visit) == n
