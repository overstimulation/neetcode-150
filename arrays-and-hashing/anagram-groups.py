from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for item in strs:
            counts = [0] * 26
            for character in item:
                index = ord(character) - ord("a")
                counts[index] += 1

            counts_as_string = str(counts)

            if counts_as_string not in result:
                result[counts_as_string] = []
            result[counts_as_string].append(item)

        return result.values()
