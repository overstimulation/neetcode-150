class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        scores = [0] * (n + 1)
        for a, b in trust:
            scores[a] -= 1
            scores[b] += 1
        for i in range(1, n + 1):
            if scores[i] == n - 1:
                return i
        return -1
