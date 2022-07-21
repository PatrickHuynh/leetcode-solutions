class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for r in range(1, len(arr)+1, 2):
            for i in range(r-1, len(arr)):
                s += sum(arr[i-r+1:i+1])
        return s