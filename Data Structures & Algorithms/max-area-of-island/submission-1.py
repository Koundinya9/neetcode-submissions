class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def crazy(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + crazy(r - 1, c) + crazy(r + 1, c) + crazy(r, c + 1) + crazy(r, c - 1)

        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    temp = crazy(r, c)
                    ans = max(ans, temp)

        return ans
        