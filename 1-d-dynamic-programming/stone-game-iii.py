class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3
        for i in range(n - 1, -1, -1):
            res = float("-inf")
            take = 0
            for j in range(3):
                if i + j < n:
                    take += stoneValue[i + j]
                    res = max(res, take - dp[(i + j + 1) % 3])
            dp[i % 3] = res

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
