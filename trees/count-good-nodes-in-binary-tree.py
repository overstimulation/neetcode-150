# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node, max_val):
            if not node:
                return 0

            is_good = 1 if node.val >= max_val else 0
            new_max_val = max(max_val, node.val)

            return is_good + count_good_nodes(node.left, new_max_val) + count_good_nodes(node.right, new_max_val)

        return count_good_nodes(root, float("-inf"))
