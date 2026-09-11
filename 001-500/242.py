class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False  
        doubled_s = s + s  # Concatenate s with itself
        return t in doubled_s  # Check if t is a substring of s + s
