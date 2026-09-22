class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def bfs(r, c):
            while q:
                row, col = q.popleft()
                directions = [(-1,0), (1,0), (0,-1), (0,1)]

                for dr, dc in directions:
                    r,c = row + dr, col + dc

                    if (
                        r in range(rows) and 
                        c in range(cols) and
                        (r,c) not in visited and
                        grid[r][c] == "1"
                    ):
                        q.append((r,c))
                        visited.add((r,c))

        # now we loop through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    q.append((r, c))
                    visited.add((r,c))
                    # find how big the island is
                    bfs(r, c)
                    islands += 1
        
        return islands