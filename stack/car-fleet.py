from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        fleets = 0
        max_time = 0

        for p, s in pairs:
            time = (target - p) / s
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets
