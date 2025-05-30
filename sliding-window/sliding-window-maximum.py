from heapq import heappop, heappush
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for i in range(len(nums)):
            heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heappop(heap)
                output.append(-heap[0][0])

        return output
