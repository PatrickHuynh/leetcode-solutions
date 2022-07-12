class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        rows = []
        cols = []
        for i in range(0, h):
            for j in range(0, w):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in rows:
            for j in range(0, w):
                matrix[i][j] = 0
        for j in cols:
            for i in range(0, h):
                matrix[i][j] = 0            
                    
        