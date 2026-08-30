#Brute-Force
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Initialize the count
        count = 0

        # Iterate through all possible starting indices
        for i in range(n):

            # Dictionary to store frequency of elements
            freq = {}

            # Iterate through all possible end indices
            for j in range(i, n):

                # Increase frequency of current element
                freq[nums[j]] = freq.get(nums[j], 0) + 1

                # If we have exactly k distinct integers, increment result
                if len(freq) == k:
                    count += 1

                # If we have more than k, stop processing further
                if len(freq) > k:
                    break

        # Return the final result
        return count