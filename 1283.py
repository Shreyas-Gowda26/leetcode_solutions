import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2

            sumBs = 0

            for x in nums:
                sumBs += math.ceil(x / mid)

            if sumBs <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low