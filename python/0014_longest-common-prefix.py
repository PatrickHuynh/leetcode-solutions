class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        i = 0
        imax = min([len(j) for j in strs])
        prefix = ''
        for i in range(imax):
            check = set([letter[i] for letter in strs])
            if len(check) == 1:
                prefix += list(check)[0]
            elif len(check) > 1:
                break
        return prefix