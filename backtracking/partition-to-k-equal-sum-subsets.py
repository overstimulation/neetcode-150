class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backtrack(i, k, subset_sum):
            if k == 0:
                return True
            if subset_sum == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or subset_sum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subset_sum + nums[j]):
                    return True
                used[j] = False
                if subset_sum == 0:
                    break
            return False

        return backtrack(0, k, 0)
