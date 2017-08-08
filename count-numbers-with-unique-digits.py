
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 9
        cur = 9
        res = 9
        for i in xrange(n - 1):
            res *= cur
            cur -= 1
        return res + self.countNumbersWithUniqueDigits(n - 1)