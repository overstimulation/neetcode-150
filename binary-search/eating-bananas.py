import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            hours_needed = 0

            for pile in piles:
                hours_needed += math.ceil(pile / mid)

            if hours_needed <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
