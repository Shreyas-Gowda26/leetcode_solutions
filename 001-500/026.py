class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer for last unique element
        i = 0

        # Traverse list starting from second element
        for j in range(1, len(nums)):
            # If current element is different from last unique one
            if nums[j] != nums[i]:
                # Move pointer forward
                i += 1
                # Place the unique element in next position
                nums[i] = nums[j]

        # i is last index of unique element, count = i + 1
        return i + 1