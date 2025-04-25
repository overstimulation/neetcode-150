from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        sorted_by_frequency = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        return [key for key, _ in sorted_by_frequency[:k]]
