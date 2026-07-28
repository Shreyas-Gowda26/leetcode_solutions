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
    

#Optimal-Approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i,j = 0, len(height)-1

        while i<j:
            width = j - i
            h = min(height[i],height[j])
            area = h * width

            max_area = max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area