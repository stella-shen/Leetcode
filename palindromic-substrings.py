class Solution(object):
    def manacher(self, s):
        s = '^#' + '#'.join(s) + '#$'
        p = [0] * len(s)
        center = 0
        right = 0
        for i in xrange(1, len(s) - 1):
            i_mirror = 2 * center - i
            if right > i:
                p[i] = min(p[i_mirror], right - i)
            while s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > right:
                center = i
                right = i + p[i]
        return p

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = self.manacher(s)
        s = 0
        for i in p:
            s += (i + 1) / 2
        return s

if __name__ == '__main__':
    sol = Solution()
    print sol.countSubstrings("aaa")
