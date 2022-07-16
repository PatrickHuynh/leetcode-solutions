class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = 0
        d1 = {}
        d2 = {}
        for c in s1:
            d1[c] = d1.get(c,0)+1
        
        for i in range(len(s2)):
            c = s2[i]
            d2[c] = d2.get(c,0) + 1
            
            if i >= len(s1):
                r = s2[i - len(s1)]
                d2[r] = d2.get(r, 0) - 1
                if d2[r] == 0:
                    del d2[r]

            if d1 == d2:
                return True
            
        return False
                
                