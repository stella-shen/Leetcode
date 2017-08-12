
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy, sell = [0] * 2, [0] * 2
        buy[0] = -prices[0]

        for i in xrange(1, len(prices)):
            buy[i % 2] = max(sell[i % 2] - prices[i], buy[(i - 1) % 2])
            sell[i % 2] = max(buy[(i - 1) % 2] + prices[i], sell[(i-1) % 2])
        return sell[(len(prices) - 1) % 2]

if __name__ == '__main__':
    print Solution().maxProfit([1, 2, 3, 0, 2])
