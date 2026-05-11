class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = 0
        while r < len(prices):
            if prices[l] < prices[r] and l != r:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
            else:
                l=r
            r+=1
        return maxProfit