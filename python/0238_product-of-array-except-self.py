class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        lcur = 1
        rcur = 1
        for i in range(0, len(nums)):
            ans[i] *= lcur
            ans[~i] *= rcur
            lcur *= nums[i]
            rcur *= nums[~i]
        
        return ans
