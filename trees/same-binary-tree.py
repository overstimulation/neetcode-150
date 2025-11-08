from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, first_tree: Optional[TreeNode], second_tree: Optional[TreeNode]) -> bool:
        if not first_tree and not second_tree:
            return True

        if not first_tree or not second_tree or first_tree.val != second_tree.val:
            return False

        return self.isSameTree(first_tree.left, second_tree.left) and self.isSameTree(
            first_tree.right, second_tree.right
        )
