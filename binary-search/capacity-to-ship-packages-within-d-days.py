class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            curr_days = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > mid:
                    curr_days += 1
                    curr_weight = w
                else:
                    curr_weight += w
            if curr_days <= days:
                r = mid
            else:
                l = mid + 1
        return l
