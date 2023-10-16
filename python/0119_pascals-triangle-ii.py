class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        else:
            prev_row = self.getRow(rowIndex - 1)
            curr_row = prev_row.copy()
            curr_row.append(1)
            for i in range(1, len(curr_row) - 1):
                curr_row[i] = prev_row[i - 1] + prev_row[i]
            return curr_row
