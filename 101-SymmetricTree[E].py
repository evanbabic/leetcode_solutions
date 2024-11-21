from typing import Optional

#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #To take recursive approach, I created a separate function that essentially checks if the left and right subtrees are the same
    #Recursively checks all subtrees, only returning True if all values are identical
    
    def isMirror(self, left_root: Optional[TreeNode], right_root: Optional[TreeNode]):
        if not left_root and not right_root:
            return True
        
        if not left_root or not right_root: 
            return False
        
        return (left_root.val == right_root.val) and self.isMirror(left_root.left, right_root.right) and self.isMirror(left_root.right, right_root.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
        




