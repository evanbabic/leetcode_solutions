# Given two binary strings a and b, return their sum as a binary string.

# Solution: Use int(a, 2) etc. to convert them to base 2 numbers, then to binary, then to a string, but shave off 0b prefix

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])