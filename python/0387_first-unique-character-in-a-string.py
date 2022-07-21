class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            c = s[i]
            d[c] = d.get(c, []) + [i]
            
        r = len(s)
        for k, v in d.items():
            if len(v) == 1:
                r = min(v[0], r)

        return -1 if r == len(s) else r
    # not the fastest but doesn't use easy in built methods