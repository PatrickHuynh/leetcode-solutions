class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = {}
        tlen = len(t)
        for c in t:
            td[c] = td.get(c, 0) + 1
        
        x = [(c, i) for i, c in enumerate(s) if c in t]
        
        sd = {}
        i = 0
        j = 0
        matched = 0
        solutions = (0,0,inf)
        while i < len(x):
            c = x[i][0]
            
            sd[c] = sd.get(c, 0) + 1
            if sd[c] <= td[c]:
                matched += 1
                
            while matched == tlen:
                substrlen = x[i][1] - x[j][1] + 1
                if substrlen < solutions[2]:
                    solutions = (x[j][1], x[i][1], substrlen)
                d = x[j][0]
                sd[d] = sd.get(d, 0) - 1
                if sd[d] < td[d]:
                    matched -= 1
                j += 1
            
            i += 1
            
        if solutions[2] == inf:
            return ""
        else:
            return s[solutions[0]:solutions[1]+1]