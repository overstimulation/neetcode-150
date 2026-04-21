class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_word = True

        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            curr = root
            for j in range(i, n):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.is_word:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]
