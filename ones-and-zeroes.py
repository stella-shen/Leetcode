
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(m + 1)] for i in xrange(n + 1)]
        for s in strs:
            ones = 0
            zeros = 0
            for c in s:
                if c == '0':
                    zeros += 1
                else:
                    ones += 1
            for i in reversed(xrange(ones, n + 1)):
                for j in reversed(xrange(zeros, m + 1)):
                    dp[i][j] = max(dp[i][j], dp[i - ones][j - zeros] + 1)
        return dp[n][m]

if __name__ == '__main__':
    print Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3)
