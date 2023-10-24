class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = str(x)
            for i in range(len(y)//2):
                if y[i] != y[-1-i]:
                    return False
            return True