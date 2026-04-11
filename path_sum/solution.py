# Definition for a binary tree node.
"""Module finding right path"""
from typing import Optional

class TreeNode:
    """Class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Class that includes function searching for the path"""
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Initialization of function named hasPathSum"""
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        else:
            left = self.hasPathSum(root.left, targetSum-root.val)
            right = self.hasPathSum(root.right, targetSum-root.val)

            return left or right
