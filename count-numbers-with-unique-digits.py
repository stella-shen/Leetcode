
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        cur = 9
        res = 10
        for i in xrange(2, n + 1):
            cur *= 10 - (i - 1)
            res += cur
        return res