#Brute-Force Approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                min_height = min(height[i], height[j])
                area = width * min_height
                max_area = max(max_area, area)

        return max_area