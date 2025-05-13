from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for index, _ in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            target = -nums[index]

            left = index + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.add((nums[index], nums[left], nums[right]))

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return [list(t) for t in result]
