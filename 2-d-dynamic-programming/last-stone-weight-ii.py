class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        target = sum(stones) // 2
        dp = [True] + [False] * target
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
        for i in range(target, -1, -1):
            if dp[i]:
                return sum(stones) - 2 * i
        return 0
