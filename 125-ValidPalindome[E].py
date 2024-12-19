# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""

        for i in s:
            if i.isalnum():
                new_string = new_string + i.lower()

        if (new_string == new_string[::-1]):
            return True
        
        else:
            return False

Test = Solution()
Test.isPalindrome("0P")