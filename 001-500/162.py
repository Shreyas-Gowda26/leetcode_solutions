#Brute
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # Traverse the array
        for i in range(n):
            # Check left neighbor if exists
            left = (i == 0) or (nums[i] >= nums[i - 1])
            # Check right neighbor if exists
            right = (i == n - 1) or (nums[i] >= nums[i + 1])

            # If both conditions are true
            if left and right:
                return i

        # In case no peak found
        return -1