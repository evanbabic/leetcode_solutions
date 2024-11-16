# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator like **.

# Solution: use a binary search to find the number that multiplies by itself to get x

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        
        while (low <= high):
            middle = (low + high) // 2

            if (middle * middle) < x:
                low = middle + 1
            
            elif (middle * middle) > x:
                high = middle - 1
        
            else:
                return middle
        
        return high