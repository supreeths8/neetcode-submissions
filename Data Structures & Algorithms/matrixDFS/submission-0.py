class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r,c, visited):
            R = len(grid)
            C = len(grid[0])

            if (r < 0 or c < 0) or (r == R or c == C) or grid[r][c] == 1 or (r,c) in visited:
                return 0
            
            if r == R - 1 and c == C - 1:
                return 1
            
            count = 0
            visited.add((r,c))
            count += dfs(r, c + 1, visited)
            count += dfs(r + 1, c, visited)
            count += dfs(r - 1, c, visited)
            count += dfs(r, c - 1, visited)

            visited.remove((r,c))

            return count
        
        return dfs(0,0,set())