class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        p = 2
        while p ** 2 <= n:
            while n % p == 0:
                res += p
                n //= p
            p += 1
        if n > 1:
            res += n
        return res