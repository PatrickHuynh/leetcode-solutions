class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = [(bin(i).count('1'), i) for i in arr]
        arr.sort()
        arr = [i[1] for i in arr]
        return arr