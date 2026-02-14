class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= i ^ n
        return res
