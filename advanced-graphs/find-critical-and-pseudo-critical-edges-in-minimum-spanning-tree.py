class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i
        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        self.components -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:
        new_edges = [[u, v, w, i] for i, (u, v, w) in enumerate(edges)]
        new_edges.sort(key=lambda x: x[2])

        def get_mst(ignore_idx=-1, force_idx=-1):
            uf = UnionFind(n)
            weight = 0
            if force_idx != -1:
                u, v, w, orig = new_edges[force_idx]
                uf.union(u, v)
                weight += w
            for i, (u, v, w, orig) in enumerate(new_edges):
                if i == ignore_idx:
                    continue
                if uf.union(u, v):
                    weight += w
            return weight if uf.components == 1 else float("inf")

        base_weight = get_mst()
        critical = []
        pseudo = []

        for i, (_, _, _, orig) in enumerate(new_edges):
            if get_mst(ignore_idx=i) > base_weight:
                critical.append(orig)
            elif get_mst(force_idx=i) == base_weight:
                pseudo.append(orig)

        return [critical, pseudo]
