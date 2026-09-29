class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dfs(r,c):
            if r >= len(grid) or c >= len(grid[0]):
                return float('inf')
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return memo[(r,c)]
        return int(dfs(0,0))