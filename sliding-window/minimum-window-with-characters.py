class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t = {}
        window = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        have = 0
        need = len(count_t)
        result = [-1, -1]
        result_length = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if (right - left + 1) < result_length:
                    result = [left, right]
                    result_length = right - left + 1

                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        left, right = result
        return s[left : right + 1] if result_length != float("inf") else ""
