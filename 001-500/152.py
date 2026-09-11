#Brute-Force approach
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]

        for i in range(len(nums)):
            prod = 1

            for j in range(i, len(nums)):
                prod *= nums[j]
                maxi = max(maxi, prod)

        return maxi