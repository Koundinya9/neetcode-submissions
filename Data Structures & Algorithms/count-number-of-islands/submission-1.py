class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def mystify(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'
            mystify(r - 1, c)
            mystify(r + 1, c)
            mystify(r, c + 1)
            mystify(r, c - 1)

            return



        rows = len(grid)
        cols = len(grid[0])

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    mystify(r, c)
                    ans += 1
        return ans
