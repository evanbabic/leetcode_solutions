# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Solution: used max depth binary tree logic (problem 104) with helper function to find 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        if (leftDepth == -1):
            return -1

        rightDepth = self.maxDepth(root.right)
        if (rightDepth == -1):
            return -1 
        
        if abs(leftDepth - rightDepth) > 1:
                return -1
        
        return 1 + max(leftDepth, rightDepth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root) != -1
