class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]
            res = []
            for j in range(i + 1, len(s) + 1):
                w = s[i:j]
                if w in wordSet:
                    for sub in dfs(j):
                        res.append(w + (" " + sub if sub else ""))
            memo[i] = res
            return res

        return dfs(0)
