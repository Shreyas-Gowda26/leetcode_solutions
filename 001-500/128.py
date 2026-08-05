class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(nums)
        if len(num)==0:
            return 0
        longest = 1
        lastSm = float('-inf')
        cnt = 0
        for i in range(0,len(num)):
            if num[i]-1 == lastSm:
                cnt+=1
                lastSm = num[i]
            elif num[i]!=lastSm:
                cnt = 1
                lastSm = num[i]
            longest = max(longest,cnt)
        return longest