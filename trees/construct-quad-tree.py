"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: list[list[int]]) -> "Node":
        def build(r, c, length):
            same = True
            for i in range(length):
                for j in range(length):
                    if grid[r + i][c + j] != grid[r][c]:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            half = length // 2
            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, len(grid))
