class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = n + 1
        for i in range(n):
            needed = prefix[i] + target
            lo, hi = i + 1, n + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] >= needed:
                    hi = mid
                else:
                    lo = mid + 1
            if lo <= n:
                res = min(res, lo - i)

        return res if res <= n else 0
