class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix = 0
        prefix_counts = {0: 1}
        for num in nums:
            prefix += num
            count += prefix_counts.get(prefix - k, 0)
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
        return count
