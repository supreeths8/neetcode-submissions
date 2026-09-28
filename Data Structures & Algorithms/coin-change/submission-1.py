class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1.0] * (amount + 1)
        def backtrack(amt):
            if amt < 0:
                return float('inf')
            if amt == 0:
                return 0
            if cache[amt] != -1:
                return cache[amt]
             
            minWays = float('inf')
            for coin in coins:
                res = 1 + backtrack(amt - coin)
                minWays = min(minWays, res)
            
            cache[amt] = minWays
            return minWays
        minWays = backtrack(amount)
        return -1 if minWays == float('inf') else int(minWays)