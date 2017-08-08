
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1
        res = 1
        if n % 3 == 0:
            res = 3 ** (n // 3)
        if n % 3 == 1:
            res = 3 ** (n // 3 - 1) * 4
        if n % 3 == 2:
            res = 3 ** (n // 3) * 2
        return res

if __name__ == '__main__':
    sol = Solution()
