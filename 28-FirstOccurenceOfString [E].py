# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or not haystack or len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)):
            if haystack[i : i + len(needle):] == needle:
                return i

        return -1

# Alternate, simplified solution (using Python)

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
