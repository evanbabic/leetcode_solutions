# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# ex: ["Flower", "Flow", "Flight"] -> "fl"

# Solution 1: Using 'startswith' method to find common prefix, reducing string by 1 character each time until common one is found

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
             return ""

        prefix = strs[0]

        for item in strs[1:]:
            while not item.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        return prefix
    
Test = Solution()
print(Test.longestCommonPrefix(["Flowers", "Flight", "Flow"]))



# Solution 2: Recursive

class Solution_Two:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        base = strs[0]

        for i in range(len(base)):
            for word in strs[1:]:
                if (i == len(word) or word[i] != base[i]):
                    return base[0:i]
        
        return base
    
Test2 = Solution_Two()
Test2.longestCommonPrefix(["Flowers", "Flight", "Flow"])
