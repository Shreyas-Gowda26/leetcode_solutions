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
    
#Optimal Approach
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        st = set(nums)
        longest = 0

        for num in st:
            # Check if num is the start of a sequence
            if num - 1 not in st:
                current = num
                length = 1

                while current + 1 in st:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest