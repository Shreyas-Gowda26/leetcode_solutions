class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        for num in freq:
            if freq[num] > n // 3:
                result.append(num)

        return result