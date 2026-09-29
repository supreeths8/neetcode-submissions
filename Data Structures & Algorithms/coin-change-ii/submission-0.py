class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, remainingAmt):
            if remainingAmt == 0:
                return 1
            if remainingAmt < 0 or i == len(coins):
                return 0
            if (i, remainingAmt) in memo:
                return memo[(i, remainingAmt)]
            
            memo[(i, remainingAmt)] = dfs(i, remainingAmt - coins[i]) + dfs(i+1, remainingAmt)
            return memo[(i, remainingAmt)]
        return dfs(0, amount)