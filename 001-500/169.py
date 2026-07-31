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
    

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>n:
                return i
            

#Optimal Moore's Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                el = nums[i]
            elif nums[i]==el:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in range(len(nums)):
            if nums[i]==el:
                cnt1+=1
        if cnt1>len(nums)//2:
            return el
        return -1