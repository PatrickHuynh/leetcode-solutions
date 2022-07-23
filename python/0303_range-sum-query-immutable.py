class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = { -1: 0 }
        runsum = 0
        for i, n in enumerate(nums):
            runsum += n
            self.presum[i] = runsum

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right] - self.presum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)