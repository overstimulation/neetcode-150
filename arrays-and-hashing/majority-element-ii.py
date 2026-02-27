class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        c1, c2, cnt1, cnt2 = 0, 1, 0, 0

        for n in nums:
            if n == c1:
                cnt1 += 1
            elif n == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1, cnt1 = n, 1
            elif cnt2 == 0:
                c2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        return [c for c in (c1, c2) if nums.count(c) > len(nums) // 3]
