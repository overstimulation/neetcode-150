import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        projects = sorted(zip(capital, profits))
        max_profit = []
        ptr = 0
        n = len(profits)

        for _ in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heapq.heappush(max_profit, -projects[ptr][1])
                ptr += 1
            if not max_profit:
                break
            w -= heapq.heappop(max_profit)

        return w
