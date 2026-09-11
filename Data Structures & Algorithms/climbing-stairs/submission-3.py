class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 2)
        # dp[0], dp[1] = 1,1

        # for i in range(2, n + 1):
        #     print(i)
        #     dp[i] = dp[i - 1] + dp[i - 2]

        dp = [1,1]
        for i in range(n-1):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp

        return dp[1]

        


            

