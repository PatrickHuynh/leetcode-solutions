class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if not self.is_valid_set(row):
                return False
        
        # check columns
        for j in range(9):
            nums = []
            for row in board:
                if row[j] != ".":
                    nums.append(row[j])
            if not self.is_valid_set(nums):
                return False
            
        # check matrices
        for i in range(3):
            for j in range(3):
                matrix = []
                for k in range(3):
                    for l in range(3):
                        x = i * 3 + k
                        y = j * 3 + l
                        matrix.append(board[x][y])
                if not self.is_valid_set(matrix):
                    return False
        return True
    
    def is_valid_set(self, nums):
        check = {}
        for num in nums:
            if num != ".":
                check[num] = check.get(num, 0) + 1
                if check[num] > 1:
                    return False
        return True