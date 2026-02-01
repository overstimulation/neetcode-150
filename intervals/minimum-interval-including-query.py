import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [-1] * len(queries)
        min_heap = []
        j = 0

        for q, idx in sorted_queries:
            while j < len(intervals) and intervals[j][0] <= q:
                left, right = intervals[j]
                heapq.heappush(min_heap, (right - left + 1, right))
                j += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                result[idx] = min_heap[0][0]

        return result
