class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0

        # Loop over all starting indices
        for start in range(len(nums)):
            # Track number of odd elements in current subarray
            oddCount = 0

            # Loop over ending indices starting from 'start'
            for end in range(start, len(nums)):
                # Check if current number is odd
                if nums[end] % 2 != 0:
                    oddCount += 1

                # If odd count exceeds k, break (not nice)
                if oddCount > k:
                    break

                # If odd count is exactly k, count this subarray
                if oddCount == k:
                    count += 1

        # Return total nice subarrays
        return count