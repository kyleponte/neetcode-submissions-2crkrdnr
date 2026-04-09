class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        L = 0
        R = 1
        while R <= len(prices) - 1:
            profit = prices[R] - prices[L]
            if profit <= 0:
                L = R
            else:
                maxProfit = max(maxProfit, profit)
            R += 1

        return maxProfit