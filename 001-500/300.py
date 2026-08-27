class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:
            low = 0
            high = len(tails)

            while low < high:
                mid = (low + high) // 2

                if tails[mid] < x:
                    low = mid + 1
                else:
                    high = mid

            if low == len(tails):
                tails.append(x)
            else:
                tails[low] = x

        return len(tails)