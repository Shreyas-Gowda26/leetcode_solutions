#Best time to buy and sell stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        n = len(prices)
        for i in range(1,n):
            cost = prices[i]-mini
            profit = max(cost,profit)
            mini = min(prices[i],mini)
        return profit 