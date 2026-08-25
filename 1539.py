class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Number of missing numbers before index mid
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1  # Need more missing values, go right
            else:
                high = mid - 1  # Too many missing, go left

        # Final k-th missing number calculation
        return k + high + 1