class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runsum = 0
        maxsum = -10**4
        for n in nums:
            runsum += n
            maxsum = max(runsum, maxsum)
            runsum = 0 if runsum < 0 else runsum
        return maxsum
