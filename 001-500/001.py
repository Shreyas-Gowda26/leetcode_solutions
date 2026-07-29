#Brute-force approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j

                # If no pair is found
        return -1,-1

#Better approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,num in enumerate(nums):
            more = target - num
            if more in mp:
                return [mp[more],i]
            mp[num]=i
        return [-1,-1]