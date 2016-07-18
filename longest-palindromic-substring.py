
class Solution(object):
    def longestPalindrome(self, s):
        """

        :type s: str
        :rtype: str
        """
        maxLen = 0
        palin = dict()
        start = 0
        end = 0
        for i in range(0, len(s)):
            palin[(i, i)] = 1
            for j in range(0, i):
                palin[(j, i)] = 0
        for i in range(0, len(s)):
            for j in range(0, i):
                if (s[i] == s[j]) and (i == j+1):
                    palin[(j, i)] = 1
                if i - 1 >= j + 1:
                    if (s[i] == s[j]) and (palin[(j+1,i-1)]):
                        palin[(j, i)] = 1
                if (palin[(j, i)] == 1) and (maxLen < i-j+1):
                    maxLen = i - j + 1
                    start = j
                    end = i
        return s[start : end + 1]

if __name__ == '__main__':
    sol = Solution()
    s = "abcbb"
    print sol.longestPalindrome(s)
