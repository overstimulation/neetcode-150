class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        dp = piles[:]
        for d in range(1, len(piles)):
            for i in range(len(piles) - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        return dp[0] > 0
