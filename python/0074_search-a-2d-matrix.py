class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return self.find_row_value(row, target)
            
        return False
                
    def find_row_value(self, row, value):
        for n in row:
            if n == value:
                return True
            if n > value:
                return False
        return False
        
    #easy mode
    def find_row_value_easy(self, row, value):
        return value in row