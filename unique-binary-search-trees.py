
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1
        for i in xrange(2, n + 1):
            for j in xrange(i):
                res[i] += res[j] * res[i - j - 1]
        return res[n]
