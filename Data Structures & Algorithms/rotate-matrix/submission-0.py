class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = COLS = len(matrix)

        for i in range(ROWS // 2):
            for j in range(COLS):
                matrix[i][j], matrix[ROWS - i - 1][j] = matrix[ROWS - i - 1][j], matrix[i][j]

        for i in range(ROWS):
            for j in range(i, COLS):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

