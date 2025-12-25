from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            visited[char] = True
            for neighbor in adj[char]:
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False
                elif visited[neighbor]:
                    return False

            visited[char] = False
            res.append(char)
            return True

        for char in sorted(adj.keys()):
            if char not in visited:
                if not dfs(char):
                    return ""

        return "".join(res[::-1])
