# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

from typing import List
from math import factorial

# Using combinations (nCr) formula to calculate each number in rows

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return_list = []

        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(factorial(i) // (factorial(j) * factorial(i-j)))
            return_list.append(row)

        return return_list

Test = Solution()
print(Test.generate(4))

