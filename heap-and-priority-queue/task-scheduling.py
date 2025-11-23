import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        q = collections.deque()

        while max_heap or q:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
