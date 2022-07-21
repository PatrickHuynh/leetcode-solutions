class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                z += 1
            else:
                nums[i-z] = nums[i]
            i += 1
        for i in range(len(nums)-z,len(nums)):
            nums[i] = 0