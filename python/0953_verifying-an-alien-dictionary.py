class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i = 1
        d = {}
        for c in order:
            d[c] = i
            i += 1
        
        if len(words) == 1:
            return True
        
        for idx, prev_word in enumerate(words[:-1]):
            word = words[idx+1]
            if prev_word == word:
                continue
            i = 0 
            while i < len(prev_word):
                if i >= len(word):
                    return False
                if prev_word[i] == word[i]:
                    i += 1
                    continue
                else:
                    if d[prev_word[i]] > d[word[i]]:
                        return False
                    else:
                        break
        
        return True
                
                
                        
                    
                