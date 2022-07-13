class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for i in str(n):
            p *= int(i)
            s += int(i)
        return p - s