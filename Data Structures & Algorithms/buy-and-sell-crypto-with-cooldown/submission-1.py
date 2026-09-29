class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            cooldown = dfs(i+1, holding)

            if holding:
                sell_res = dfs(i+2, False) + prices[i]
                sell_res = max(sell_res, cooldown)
                memo[(i, holding)] = sell_res
                return sell_res
            else:
                buy_res = dfs(i+1, True) - prices[i]
                buy_res = max(buy_res, cooldown)
                memo[(i, holding)] = buy_res
                return buy_res
        return dfs(0, False)