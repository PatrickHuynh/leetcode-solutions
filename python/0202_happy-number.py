class Solution:
    def isHappy(self, n: int) -> bool:
        prev_nums = set()
        while True:
            s = 0
            for i in str(n):
                s += int(i)**2
            if s == 1:
                return True
            else:
                if s in prev_nums:
                    return False
                else:
                    prev_nums.add(s)
                n = s
                