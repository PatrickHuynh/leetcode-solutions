class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        xlen = len(mat)
        x = 0
        y = xlen - 1
        s = 0
        while x < xlen:
            s += mat[x][x]
            s += mat[x][y] if x != y else 0
            x += 1
            y -= 1
        return s