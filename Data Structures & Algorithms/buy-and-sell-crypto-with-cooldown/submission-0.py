class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buy):
            
            # Going out of bounds - return 0 
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            
            # Do not buy/sell today
            cooldown = dfs(i+1, buy)
            if buy:
                buy_res = dfs(i+1, not buy) - prices[i]
                memo[(i,buy)] = max(buy_res, cooldown)
                return memo[(i,buy)]
            else:
                sell_res = dfs(i+2, not buy) + prices[i]
                memo[(i,buy)] = max(sell_res, cooldown)
                return memo[(i,buy)]
        
        return dfs(0, True)