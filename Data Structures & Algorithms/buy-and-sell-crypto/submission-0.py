class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        for i in range(len(prices)):
            maxprofit=max(maxprofit,max(prices[i:])-prices[i])
        return maxprofit

        