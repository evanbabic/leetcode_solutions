# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution: add root value to left and right nodes, and keep moving down until we find a leaf node and see if it equals targetSum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if (root.val == targetSum and root.left == None and root.right == None):
            return True
        
        if (root.left != None):
            root.left.val += root.val

        if (root.right != None):
            root.right.val += root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)