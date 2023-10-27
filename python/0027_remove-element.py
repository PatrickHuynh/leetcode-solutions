class Solution:
    def removeElement(self, nums: List[int], val: int):
        count = len(nums)
        i = 0
        k = 0
        for j in range(0,count):
            if nums[j] != val:
                nums[i] = nums[j]
                k += 1
                i += 1
        return k