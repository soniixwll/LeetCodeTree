# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    """Class TReeNode"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Class fot evaluating the Tree"""
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """Function that evaluates the tree using recursion"""
        if root.val in (0, 1):
            return bool(root.val)

        else:
            left = self.evaluateTree(root.left)
            right = self.evaluateTree(root.right)

            if root.val == 2:
                return left or right
            else:
                return left and right
