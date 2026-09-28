class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def backtrack(amt):
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            minWays = 1e9
            for coin in coins:
                if amt - coin >= 0:
                    minWays = min(minWays, 1 + backtrack(amt - coin))
            memo[amt] = minWays
            return minWays
        
        minWays = backtrack(amount)
        return -1 if minWays == 1e9 else int(minWays)
                
            

