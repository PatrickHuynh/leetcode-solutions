class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        len_rows = len(mat)
        len_cols = len(mat[0])

        res = [[len_cols+len_rows for c in range(len_cols)] for r in range(len_rows)]

        for r in range(len_rows):
            for c in range(len_cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                else:
                    res[r][c] = min(res[max(r-1, 0)][c]+1, res[r][max(c-1, 0)]+1)

        for r in reversed(range(len_rows)):
            for c in reversed(range(len_cols)):
                if res[r][c] != 0:
                    res[r][c] = min(res[r][c], res[min(r+1, len_rows-1)][c]+1, res[r][min(c+1, len_cols-1)]+1)

        return res
