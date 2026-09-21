class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #1st approach
        for i in range(len(haystack) - len(needle) + 1):

            if haystack[i:i + len(needle)] == needle:
                return i

        return -1



    #Built-in
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)