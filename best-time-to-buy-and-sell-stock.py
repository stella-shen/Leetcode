class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        low = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            max_profit = max(max_profit, prices[i] - low)
        
        return max_profit
