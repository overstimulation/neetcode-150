from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            curr, turns = q.popleft()
            if curr == target:
                return turns

            for i in range(4):
                digit = int(curr[i])
                for move in [-1, 1]:
                    new_state = curr[:i] + str((digit + move) % 10) + curr[i + 1 :]
                    if new_state not in dead_set and new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, turns + 1))

        return -1
