class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def backtrack(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i+1] = backtrack(i+1)
            memo[i+2] = backtrack(i+2)
            return memo[i+1] + memo[i+2]
            
        return backtrack(0)