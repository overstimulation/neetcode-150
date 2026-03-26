class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(largest):
            subarray_count = 1
            cur_sum = 0
            for n in nums:
                cur_sum += n
                if cur_sum > largest:
                    subarray_count += 1
                    cur_sum = n
            return subarray_count <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
