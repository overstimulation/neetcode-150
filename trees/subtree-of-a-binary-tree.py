from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not sub_root:
            return True
        if not root:
            return False

        if self.is_same_tree(root, sub_root):
            return True

        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
