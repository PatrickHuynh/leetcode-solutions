class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = (l+r) // 2
        while True:
            if target == nums[m]:
                return m
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            elif target < nums[m]:
                r = m
            elif target > nums[m]:
                l = m
            m = (l+r) // 2
            if m == l:
                return -1