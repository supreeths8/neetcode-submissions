class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        R = len(grid)
        C = len(grid[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c)
                    maxArea = max(area, maxArea)
        
        return maxArea




