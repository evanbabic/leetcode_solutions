# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

from typing import List
from math import factorial

# Using combinations (nCr) formula to calculate each number in rows
# More efficient than previous solution, deriving each element from the previous one

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return_list = [1]

        for j in range(1, rowIndex+1):
            next_element = return_list[j - 1] * (rowIndex - j + 1) // j
            return_list.append(next_element)

        return return_list

Test = Solution()
print(Test.getRow(3))
