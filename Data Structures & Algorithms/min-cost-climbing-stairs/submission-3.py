class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def backtrack(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(backtrack(i+1), backtrack(i+2))
            return memo[i]
        return min(backtrack(0), backtrack(1))
            