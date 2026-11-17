class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        rows = len(heights)
        cols = len(heights[0])

        po = [[False] * cols for _ in range(rows)]
        
        ao = [[False] * cols for _ in range(rows)]

        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True

                for i, j in directions:
                    nr, nc = i + r, j + c

                    if 0 <= nr < rows and 0 <= nc < cols and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))

        pac = []
        atl = []

        for i in range(cols):
            pac.append((0, i))
            atl.append((rows - 1, i))

        for i in range(rows):
            pac.append((i, 0))
            atl.append((i, cols - 1))

        
        bfs(pac, po)
        bfs(atl, ao)

        ans = []

        for i in range(rows):
            for j in range(cols):
                if po[i][j] and ao[i][j]:
                    ans.append([i, j])


        return ans

        

