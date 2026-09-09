class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if strings are of the same length
        if len(s) != len(goal):
            return False  

        # Try all possible rotations of s
        for i in range(len(s)):
            # Generate a rotated version of s
            rotated = s[i:] + s[:i]  
            # If the rotated version matches goal, return True
            if rotated == goal:
                return True  

        # If no rotation matches, return False
        return False 