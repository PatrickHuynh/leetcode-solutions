class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        lsum = 0
        rsum = sum(nums[i+1:])
        while i < len(nums):
            if lsum == rsum:
                return i
            lsum += nums[i]
            if i+1 < len(nums):
                rsum -= nums[i+1]
            i += 1
        return -1