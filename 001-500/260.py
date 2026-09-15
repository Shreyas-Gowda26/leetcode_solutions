#Brute-Force Solution
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count == 1:
                result.append(nums[i])
        return result