# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

# Optimized Solution ( O(n) )

class Solution:
    def twoSum(self, nums, target) -> list[int]:
        seen = {}                                   # Keeps track of visited numbers

        for i in range(len(nums)):                  # Loops through list
            diff = target - nums[i]                 # If x + y = target,  target - y = x

            if diff in seen:                        # If diff has already been seen, we found the pair to get the sum
                return [seen[diff], i]
            else:
                seen[nums[i]] = i                   # Otherwise, add i to the next index in seen dictionary (keeping track of its index and value)


# The brute force method would be to add every single number in the list together ( O(n^2) )