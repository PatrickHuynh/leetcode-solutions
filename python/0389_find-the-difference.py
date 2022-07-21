class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(s)
        b = sorted(t)
        for i in range(len(b)):
            if i >= len(a):
                return b[i]
            if a[i] != b[i]:
                return b[i] # always will have a letter in random position so don't need to handle other conditions