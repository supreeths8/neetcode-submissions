class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = 0
        sell_ptr = 0
        P = 0

        while sell_ptr < len(prices):
            if prices[sell_ptr] <= prices[buy_ptr]:
                buy_ptr = sell_ptr
            else:
                P = max(P, prices[sell_ptr] - prices[buy_ptr])
            sell_ptr += 1
        
        return P

