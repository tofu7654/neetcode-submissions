class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            # start the bfs from this new island and find island size
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # look at island/water around
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and
                        c in range(cols) and 
                        (r,c) not in visited and
                        grid[r][c] == "1"):

                        visited.add((r,c))
                        q.append((r,c))


        # island finder
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # find out how large the island is
                    bfs(r, c)
                    islands += 1
        
        return islands