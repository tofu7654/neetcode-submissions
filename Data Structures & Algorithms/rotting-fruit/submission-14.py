class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()
        visited = set()

        # find the fresh and rotten
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        # do the bfs from the rotten fruits
        while q and fresh > 0: 
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                
                    if (
                        r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and 
                        grid[r][c] not in visited
                    ):
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
                        visited.add((r,c))
            time += 1
        
        if fresh > 0:
            return -1
        else:
            return time




