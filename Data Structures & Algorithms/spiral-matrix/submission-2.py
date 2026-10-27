class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = "right"

        ans = []

        ROWS, COLS = len(matrix), len(matrix[0])

        seen = set()

        i = j = 0

        while len(ans) < ROWS * COLS:
            ans.append(matrix[i][j])
            seen.add((i, j))
            if dir == "right":
                if j + 1 == COLS or (i, j + 1) in seen:
                    dir = "down"
                    i += 1
                else:
                    j += 1
            elif dir == "down":
                if i + 1 == ROWS or (i + 1, j) in seen:
                    dir = "left"
                    j -= 1
                else:
                    i += 1
            elif dir == "left":
                if j - 1 < 0 or (i, j - 1) in seen:
                    dir = "up"
                    i -= 1
                else:
                    j -= 1
            else:
                if i - 1 < 0 or (i - 1, j) in seen:
                    dir = "right"
                    j += 1
                else:
                    i -= 1
            
        return ans
                