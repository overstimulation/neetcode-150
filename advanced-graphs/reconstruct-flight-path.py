from typing import List
import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)

        dfs("JFK")
        return res[::-1]
