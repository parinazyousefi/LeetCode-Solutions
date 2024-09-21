# max profit: lowest buy , highest sale
# prices[a] < prices[b]   ====> a< b (we first buy and then sell)
# prices = [7,1,5,3,6,4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(profit, maxProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit
