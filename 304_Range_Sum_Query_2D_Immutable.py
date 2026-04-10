class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        # prefix[i][j] = sum of rectangle (0,0) -> (i-1, j-1)
        # extra row/col of zeros simplifies boundary handling
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (
                    matrix[i-1][j-1]
                    + self.prefix[i-1][j]
                    + self.prefix[i][j-1]
                    - self.prefix[i-1][j-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        P = self.prefix
        return (
            P[row2+1][col2+1]
            - P[row1][col2+1]
            - P[row2+1][col1]
            + P[row1][col1]
        )