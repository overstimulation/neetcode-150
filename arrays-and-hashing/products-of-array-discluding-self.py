from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     result = []

    #     for num in nums:
    #         product = 1
    #         for i in range(len(nums)):
    #             if num == nums[i]:
    #                 continue
    #             product *= nums[i]
    #         result.append(product)

    #     return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n
        left_product = 1
        right_product = 1

        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
