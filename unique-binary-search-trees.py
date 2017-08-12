
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        def combination(n, k):
            res = 1
            for i in xrange(k):
                res *= (n - i)
                res /= (i + 1)
            return res

        return combination(2 * n, n) - combination(2 * n, n - 1)
