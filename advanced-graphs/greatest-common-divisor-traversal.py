class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False

        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        parent = list(range(n))
        size = [1] * n

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                return 1
            return 0

        prime_to_index = {}
        components = n

        for i, val in enumerate(nums):
            curr = val
            while curr > 1:
                p = spf[curr]
                if p in prime_to_index:
                    components -= union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i
                while curr % p == 0:
                    curr //= p

        return components == 1
