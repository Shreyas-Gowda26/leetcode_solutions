#Brute-Force approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        b = n//2
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[j]==nums[i]:
                    cnt+=1
            if cnt>b:
                return nums[i]
        return -1