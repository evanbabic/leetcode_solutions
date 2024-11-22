# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.

#Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Solution: find the middle element (as the array is sorted), and recursively build left and right subtrees

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        middle = len(nums)//2
        left = nums[:middle]
        right = nums[middle + 1:]
        
        root = TreeNode(val = nums[middle])
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root