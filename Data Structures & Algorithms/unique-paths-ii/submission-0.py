class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        def dfs(r,c):
            if r == len(obstacleGrid) or c == len(obstacleGrid[0]):
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
                return 1
            if memo[r][c] != -1:
                return memo[r][c]
            

            memo[r][c] = dfs(r+1, c) + dfs(r, c + 1)
            return memo[r][c]
        
        return dfs(0,0)