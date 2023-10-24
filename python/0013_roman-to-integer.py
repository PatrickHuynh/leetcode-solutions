class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        prev_val = 0
        curr_val = 0
        value = 0
        for i in range(len(s)):
            curr_val = values[s[-1-i]]
            if curr_val >= prev_val:
                value += curr_val
            else:
                value -= curr_val
            prev_val = curr_val       
        return value