class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        dist = 0
        while q:
            dist += 1
            for i in range(len(q)):
                r, c = q.popleft()

                if r + 1 < rows and grid[r + 1][c] == 2147483647:
                    grid[r + 1][c] = dist
                    q.append((r + 1, c))
                
                if r - 1 >= 0 and grid[r - 1][c] == 2147483647:
                    grid[r - 1][c] = dist
                    q.append((r - 1, c))


                if c + 1 < cols and grid[r][c + 1] == 2147483647:
                    grid[r][c + 1] = dist
                    q.append((r, c + 1))


                if c - 1 >= 0 and grid[r][c - 1] == 2147483647:
                    grid[r][c - 1] = dist
                    q.append((r, c - 1))


        