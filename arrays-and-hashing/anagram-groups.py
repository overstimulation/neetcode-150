from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for string in strs:
            counts = [0] * 26

            for character in string:
                counts[ord(character) - ord("a")] += 1

            counts_as_tuple = tuple(counts)

            if counts_as_tuple not in result:
                result[counts_as_tuple] = []
            result[counts_as_tuple].append(string)

        return result.values()
