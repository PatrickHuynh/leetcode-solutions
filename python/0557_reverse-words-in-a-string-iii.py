class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([''.join(reversed(list(k))) for k in s.split(" ")])