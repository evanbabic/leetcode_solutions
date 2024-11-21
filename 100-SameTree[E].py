from typing import Optional

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #If root is null for both, trees are empty and therefore equal
        if not p and not q:
            return True
    
        #If one is null and the other isn't, they are not equal
        if not p or not q:
            return False
        
        #Use pre-order traversal (root,left,right) with three conditional statements to check left and right subtrees
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
