class Solution:
    def hammingWeight(self, n: int) -> int:
        w = 0
        for i in str(bin(n)):
            if i == "1":
                w += 1
        return w