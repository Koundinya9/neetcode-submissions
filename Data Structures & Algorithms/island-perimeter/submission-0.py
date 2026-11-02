class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    sides = 4

                    if i + 1 < ROWS:
                        if grid[i + 1][j] == 1:
                            sides -= 1
                    
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            sides -= 1

                    if j + 1 < COLS:
                        if grid[i][j + 1] == 1:
                            sides -= 1

                    if j - 1 >= 0:
                        if grid[i][j - 1] == 1:
                            sides -= 1

                    ans += sides

        return ans