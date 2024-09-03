class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #### thoughts
        # 2 pointers buy and sell, b set to 1st element
        # keep track of max_profit, set as 0
        # for sell in prices from 2nd element, if sell > buy, buy=sell, else:else update max_profit
        # return max_profit
        # O(n), O(1)
        ### edge cases
        # if len prices 1, return 0
        # if reverse sorted, return 0

        buy, sell = 0, 1
        profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profit
