from typing import Optional, List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Solution: recursive approach to navigate all the way to leftmost node, add its value to list, and move up tree 'inorder' ie. left->root->right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        