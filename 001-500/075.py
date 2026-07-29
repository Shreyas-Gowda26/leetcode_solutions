#Brute-Force
#We can sort the array using merge sort which has the time complexity of nlogn

#Better Approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for i in range(len(nums)):
            if nums[i]==0:
                cnt0+=1
            elif nums[i]==1:
                cnt1+=1
            else:
                cnt2+=1
        
        for i in range(cnt0):
            nums[i]=0
        for i in range(cnt0,cnt0+cnt1):
            nums[i] = 1
        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2
