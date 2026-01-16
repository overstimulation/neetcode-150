class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for l in range(n - length):
                r = l + length
                for i in range(l + 1, r):
                    coins = nums[l] * nums[i] * nums[r]
                    coins += dp[l][i] + dp[i][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[0][n - 1]
