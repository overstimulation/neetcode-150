from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = [set() for _ in range(9)]
        cols_seen = [set() for _ in range(9)]
        boxes_seen = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell != ".":
                    if cell in rows_seen[row]:
                        return False
                    rows_seen[row].add(cell)
                    if cell in cols_seen[col]:
                        return False
                    cols_seen[col].add(cell)
                    box_index = (row // 3) * 3 + (col // 3)
                    if cell in boxes_seen[box_index]:
                        return False
                    boxes_seen[box_index].add(cell)

        return True
