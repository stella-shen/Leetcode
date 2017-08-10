
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        dp = list()
        for i in xrange(len(s)):
            cur_list = list()
            for j in xrange(len(s)):
                cur_list.append(0)
            dp.append(cur_list)
            
        for i in reversed(xrange(len(s))):
            dp[i][i] = 1
            for j in xrange(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindromeSubseq("bbbab")
