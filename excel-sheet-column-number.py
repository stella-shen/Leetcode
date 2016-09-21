
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i in xrange(len(s)):
            ret *= 26
            ret += ord(s[i]) - ord('A') + 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    s = "AB"
    print sol.titleToNumber(s)
