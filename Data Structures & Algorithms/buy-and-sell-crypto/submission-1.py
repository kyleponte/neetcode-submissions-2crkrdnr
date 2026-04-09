class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        L, R = 0, 1
        while R < len(prices):
            if prices[R] <= prices[L]:
                L = R
            else:
                maxProfit = max(maxProfit, prices[R] - prices[L])
            R += 1

        return maxProfit