class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dfs(r,c, prev_val):
            if r == len(matrix) or c == len(matrix[0]) or r < 0 or c < 0:
                return 0
            if matrix[r][c] <= prev_val:
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]


            memo[(r,c)] = 1 + max(dfs(r + 1, c, matrix[r][c]), dfs(r, c + 1, matrix[r][c]), dfs(r -1, c, matrix[r][c]), dfs(r, c - 1, matrix[r][c]))


            return memo[(r,c)]
        
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c, -1))

        return res
