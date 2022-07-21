class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while True:
            m = (l+r)//2            
            if nums[m] == target:
                return m
            if target < nums[m]:
                r = m
                if l == r:
                    return l
            else:
                l = m+1
                if l > r:
                    return l
            