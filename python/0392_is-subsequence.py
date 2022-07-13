class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s = list(s)
        for i in range(0, len(t)):
            if t[~i] == s[-1]:
                s.pop()
                if len(s) == 0:
                    return True
        return False