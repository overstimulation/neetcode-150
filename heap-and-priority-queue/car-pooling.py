class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        changes = [0] * 1001
        for num, start, end in trips:
            changes[start] += num
            changes[end] -= num

        curr = 0
        for change in changes:
            curr += change
            if curr > capacity:
                return False
        return True
