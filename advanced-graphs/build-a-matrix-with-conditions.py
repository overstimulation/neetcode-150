from collections import defaultdict, deque


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]
    ) -> list[list[int]]:
        def top_sort(conditions):
            adj = defaultdict(list)
            indegree = {i: 0 for i in range(1, k + 1)}
            for u, v in conditions:
                adj[u].append(v)
                indegree[v] += 1

            q = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            return order if len(order) == k else []

        row_order = top_sort(rowConditions)
        col_order = top_sort(colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {n: i for i, n in enumerate(row_order)}
        col_pos = {n: i for i, n in enumerate(col_order)}

        ans = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            ans[row_pos[i]][col_pos[i]] = i

        return ans
