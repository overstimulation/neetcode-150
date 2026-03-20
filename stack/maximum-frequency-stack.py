class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        new_freq = self.freq.get(val, 0) + 1
        self.freq[val] = new_freq

        if new_freq > self.max_freq:
            self.max_freq = new_freq

        if new_freq not in self.group:
            self.group[new_freq] = []
        self.group[new_freq].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val
