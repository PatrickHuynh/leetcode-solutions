class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        imax = max(len(word1), len(word2))
        for i in range(imax):
            if i < len(word1):
                output.append(word1[i])
            if i < len(word2):
                output.append(word2[i])
        return ''.join(output)