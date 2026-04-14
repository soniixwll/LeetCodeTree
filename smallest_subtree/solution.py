# Definition for a binary tree node.
"""Module finding the smallest subtree of the deepest nodes"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_the_deepest(self, root: Optional[TreeNode], depth=0):
        if root is None:
            return 0, root
        else:
            left_depth, left_node = self.find_the_deepest(root.left, depth+1)
            right_depth, right_node = self.find_the_deepest(root.right, depth+1)

            if left_depth > right_depth:
                return left_depth+1, left_node
            elif left_depth < right_depth:
                return right_depth+1, right_node
            else:
                return left_depth+1, root


    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.find_the_deepest(root)[1]
