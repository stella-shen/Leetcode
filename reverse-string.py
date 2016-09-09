
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[ : : -1]

if __name__ == '__main__':
    sol = Solution()
    s = "A man\nA plan"
    print sol.reverseString(s)
