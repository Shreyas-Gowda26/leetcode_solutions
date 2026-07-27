class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n):
            num = nums[i]
            cnt = 0
            for j in range(0,n):
                if nums[j]==num:
                    cnt +=1
            if cnt == 1:
                return num