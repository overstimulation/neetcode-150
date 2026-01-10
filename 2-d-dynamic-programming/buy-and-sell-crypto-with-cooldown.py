class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        held, sold, reset = float("-inf"), 0, 0

        for price in prices:
            held, sold, reset = max(held, reset - price), held + price, max(reset, sold)

        return max(sold, reset)
