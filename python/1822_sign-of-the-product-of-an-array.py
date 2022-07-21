class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for i in nums:
            p = -p if i < 0 else p
            if i == 0:
                return 0
        return p
