class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapleft = {}
        mapright = {}
        for i, a in enumerate(s):
            b = t[i]
            if a in mapleft and mapleft[a] != b:
                return False
            if b in mapright and mapright[b] != a:
                return False
            mapleft[a] = b
            mapright[b] = a            
        return True
            
        