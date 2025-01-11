# 169. Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        counter = 0

        for i in nums:
            if (counter == 0):
                majority_element = i
                counter += 1

            elif (i == majority_element):
                counter += 1

            else:
                counter -= 1
        
        return majority_element



            

