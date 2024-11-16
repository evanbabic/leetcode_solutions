# Given an integer x, return true if x is a palindrome, and false otherwise.

# Simple Solution - uses string slicing ::-1 to reverse the string, then compare.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        
        return string == string[::-1]

Test = Solution()
print(Test.isPalindrome(100001))


