class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            comparator = {}
            for w in s:
                comparator[w] = comparator.get(w,0) + 1
            for w in t:
                comparator[w] = comparator.get(w,0) - 1
                if comparator[w] < 0:
                    return False
        return True
        