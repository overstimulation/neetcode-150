import collections


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}
        self.freq_to_keys = collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        val, freq = self.key_to_val_freq[key]

        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1

        self.key_to_val_freq[key][1] = freq + 1
        self.freq_to_keys[freq + 1][key] = None

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self.get(key)
            return

        if len(self.key_to_val_freq) == self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]

        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
