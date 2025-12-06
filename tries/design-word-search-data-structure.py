class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["is_end_of_word"] = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr:
                        if child != "is_end_of_word" and dfs(i + 1, curr[child]):
                            return True
                    return False
                else:
                    if c not in curr:
                        return False
                    curr = curr[c]
            return "is_end_of_word" in curr

        return dfs(0, self.root)
