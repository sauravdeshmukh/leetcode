class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #### thoughts
        # 2 pointers, set buy at 0 and sell at 1, profit as 0
        # for sell in prices from 1, if value at sell > value at buy, add to profit, buy=sell
        # else buy=sell
        # O(n), O(1)
        ### edge cases
        # if len prices 1, then return 0
        # if prices reverse sorted, return 0        
        buy, sell = 0, 1
        profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit += prices[sell] - prices[buy]
            buy = sell
            sell += 1
        return profit
