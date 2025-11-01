from typing import Optional


class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict[int, Node] = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: Node) -> None:
        if node.prev and node.next:
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev

    def _insert(self, node: Node) -> None:
        if self.right.prev:
            prev, nxt = self.right.prev, self.right
            prev.next = node
            nxt.prev = node
            node.next = nxt
            node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            if lru:
                self._remove(lru)
                del self.cache[lru.key]
