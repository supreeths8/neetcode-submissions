class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        if grid[0][0] == 1 or grid[R-1][C-1] == 1:
            return -1

        visited = set()
        queue = deque()

        visited.add((0,0))
        queue.append((0,0))

        L = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == R - 1 and c == C - 1:
                    return L
                
                neighbours = [[-1, 0], [1,0], [0,-1], [0,1]]
                for dr, dc in neighbours:
                    if r + dr < 0 or c + dc < 0 or r + dr == R or c + dc == C or (r+dr, c+dc) in visited or grid[r+dr][c+dc] == 1:
                        continue
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr,c+dc))
            
            L += 1
        return -1
            









