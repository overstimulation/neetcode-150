from collections import defaultdict


class CountSquares:
    def __init__(self):
        self.pts = defaultdict(int)
        self.pts_list = []

    def add(self, point: list[int]) -> None:
        self.pts[tuple(point)] += 1
        self.pts_list.append(point)

    def count(self, point: list[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.pts_list:
            dist = abs(py - y)
            if dist == 0 or abs(px - x) != dist:
                continue
            res += self.pts[(x, py)] * self.pts[(px, y)]
        return res
