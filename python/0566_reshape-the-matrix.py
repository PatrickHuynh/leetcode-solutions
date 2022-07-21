class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mx = len(mat[0])
        my = len(mat)
        
        if mx * my != r * c:
            return mat
        
        res = [[0 for k in range(c)] for l in range(r)]
        
        rx = ry = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = mat[ry][rx]
                rx += 1
                if rx == mx:
                    rx = 0
                    ry += 1
        return res