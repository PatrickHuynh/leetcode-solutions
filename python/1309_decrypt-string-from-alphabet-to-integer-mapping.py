class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        charmap = {}
        for i in range(len(alphabet)):
            charmap[str(i+1)] = alphabet[i]
        parse = []
        readnum = False
        numcount = 0
        num = ''
        for i in reversed(range(len(s))):
            if s[i] == "#":
                readnum = True
                numcount = 0
                num = ""
            
            if readnum:
                numcount += 1
                if numcount == 3:
                    num = s[i:i+2]
                    parse.append(charmap[num])
                    readnum = False
            else:
                parse.append(charmap[str(s[i])])
        
        return ''.join(reversed(parse))
                    