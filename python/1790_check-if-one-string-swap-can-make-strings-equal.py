class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff = None
        closed = True
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff is None:
                    diff = [s1[i], s2[i]]
                    closed = False
                else:
                    if s1[i] != diff[1] or s2[i] != diff[0]:
                        return False
                    else:
                        diff = [0,0]
                        closed = True
        if not closed:
            return False
        return True
