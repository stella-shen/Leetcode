
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        lower = list()
        upper = list()
        for i in range(26):
            lower.append(0)
            upper.append(0)
        for c in s:
            if c.isupper():
                upper[ord(c) - ord('A')] += 1
            elif c.islower():
                lower[ord(c) - ord('a')] += 1
        flag = False
        for i in upper:
            if i % 2 == 0:
                res += i
            else:
                res += i - 1
                flag = True
        for i in lower:
            if i % 2 == 0:
                res += i
            else:
                res += i - 1
                flag = True
        if flag:
            res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindrome("abccccdd")
