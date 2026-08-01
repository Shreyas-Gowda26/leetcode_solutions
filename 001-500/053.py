#Optimal Approach using Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        n = len(nums)
        su = 0
        for i in range(n):
            su += nums[i]
            if su>maxi:
                maxi = su
            if su<0:
                su = 0
        return maxi
    
#Better Approach
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        for i in range(len(nums)):
            su = 0
            for j in range(i,len(nums)):
                su += nums[i]
                maxi = max(su,maxi)
        return maxi
