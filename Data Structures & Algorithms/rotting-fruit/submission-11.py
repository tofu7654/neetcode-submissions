class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        q = deque()
        rows, cols = len(grid), len(grid[0])

        # get fresh and rotten positions
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # start the bfs
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (
                        r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == 1
                    ):
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
            time += 1
        
        if fresh > 0:
            return -1
        else:
            return time
            