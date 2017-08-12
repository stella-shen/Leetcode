
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths(n, m)
        ways = [1] * m

        for i in xrange(1, m):
            for j in xrange(1, n):
                ways[j] += ways[j - 1]

        return ways[n - 1]

if __name__ == '__main__':
    sol = Solution()
    print sol.uniquePaths(3, 7)
