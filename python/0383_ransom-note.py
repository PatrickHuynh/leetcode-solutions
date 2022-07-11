class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mdict = {}
        for m in magazine:
            mdict[m] = mdict.get(m,0) + 1
            
        for c in ransomNote:
            mdict[c] = mdict.get(c,0) - 1
            if mdict[c] < 0:
                return False
        return True