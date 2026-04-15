class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                curr.append(nums[i])
                backtrack()
                curr.pop()
                used[i] = False

        backtrack()
        return res
