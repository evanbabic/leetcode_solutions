# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# To achieve optimal space and time complexity, we can use bitwise operations, specifically XOR
# Notably, any number XOR itself is 0, and any number XOR 0 is itself
# In Python, we use ^ to perform XOR

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        duplicate = 0

        for i in nums:
            duplicate ^= i
        
        return duplicate
