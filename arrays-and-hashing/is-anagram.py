class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            counts[index] += 1

        for char in t:
            index = ord(char) - ord("a")
            counts[index] -= 1
            if counts[index] < 0:
                return False

        return True
