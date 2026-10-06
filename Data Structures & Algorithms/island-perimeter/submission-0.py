class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()

        perimeter = 0

        def dfs(r,c):
            nonlocal perimeter
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] == 0:
                perimeter += 1
                return
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c + 1)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
        return perimeter