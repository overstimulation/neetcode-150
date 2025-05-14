from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best_result = 0

        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])
            if current_area > best_result:
                best_result = current_area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best_result
