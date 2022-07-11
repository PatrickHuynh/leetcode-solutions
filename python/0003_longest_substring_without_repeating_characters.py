class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_chr = {}
        start = maxlen = 0
        for idx, ch in enumerate(s):
            if ch in used_chr and start <= used_chr[ch]:
                start = used_chr[ch] + 1
            maxlen = max(maxlen, idx - start + 1)
            used_chr[ch] = idx
        return maxlen
            
            