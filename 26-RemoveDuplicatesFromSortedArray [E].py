from typing import List

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0

        for j in range(1, len(nums)):

            if(nums[j] != nums[i]):
                i += 1
                nums[i] = nums[j]

        return i + 1
    

nums = [0,0,1,1,1,2,2,3,3,4]
Test1 = Solution()
print(Test1.removeDuplicates(nums))
