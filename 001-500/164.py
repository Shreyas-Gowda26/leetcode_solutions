class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        maxDiff = 0
        if n<2:
            return 0
        nums.sort()
        for i in range(n-1):
            diff = nums[i+1]-nums[i]
            maxDiff = max(maxDiff,diff)
        return maxDiff