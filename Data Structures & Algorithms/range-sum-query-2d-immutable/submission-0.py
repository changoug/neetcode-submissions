class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = []
        for r in range(len(matrix)):
            self.matrix.append([0] * len(matrix[0]))
            for c in range(len(matrix[0])):
                top = (0 if r == 0 else self.matrix[r - 1][c])
                left = (0 if c == 0 else self.matrix[r][c - 1])
                diag = (0 if c == 0 or r == 0 else self.matrix[r - 1][c - 1])
                self.matrix[r][c] = matrix[r][c] + top + left - diag
            print(self.matrix[r])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = 0 if row1 == 0 else self.matrix[row1 - 1][col2]
        left = 0 if col1 == 0 else  self.matrix[row2][col1 - 1]
        diag = 0 if col1 == 0 or row1 == 0 else self.matrix[row1 - 1][col1 - 1]
        bottom_right = self.matrix[row2][col2]
        return bottom_right - top - left + diag

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)