from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1
        leaves = deque([i for i in range(n) if degree[i] == 1])
        while n > 2:
            size = len(leaves)
            n -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)
