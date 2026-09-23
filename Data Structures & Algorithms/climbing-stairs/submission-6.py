class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def dp(i):
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = dp(i+1) + dp(i+2)
        #     return memo[i]
        
        dpa = [0] * (n+1)
        dpa[0] = 1
        dpa[1] = 1

        for i in range(2, n+1):
            dpa[i] = dpa[i - 1] + dpa[i - 2]

        return dpa[n]
        