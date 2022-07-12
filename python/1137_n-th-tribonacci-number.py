class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1, 2]
        if n > 3:
            for i in range(4, n+1):
                a = [*a[1:],sum(a[1:])]
        else:
            return a[n]
        return a[3]