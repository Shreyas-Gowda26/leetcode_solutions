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
    
#Optimal Approach with O(nlogn)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:    return 0
        if nums[0]>nums[1]: return 0
        if nums[n-1]>nums[n-2]: return n-1
        low = 1
        high = n-2
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                low = mid+1
            else:
                high = mid -1

        return -1