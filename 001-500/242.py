class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False  
        doubled_s = s + s  # Concatenate s with itself
        return goal in doubled_s  # Check if goal is a substring of s + s
        