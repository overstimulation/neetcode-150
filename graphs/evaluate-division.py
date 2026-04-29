from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            q = deque([(src, 1.0)])
            visit = {src}
            while q:
                n, w = q.popleft()
                if n == dst:
                    return w
                for nei, weight in graph[n].items():
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, w * weight))
            return -1.0

        return [bfs(q[0], q[1]) for q in queries]
