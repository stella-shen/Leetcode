
class Solution(object):
    def preprocess(self, s):
        """

        :type s: str
        :rtype: str
        """
        if s == "":
            return "^$"
        ret = "^"
        for c in s:
            ret += "#" + c
        ret += "#$"
        return ret

    def longestPalindrome(self, s):
        """

        :type s: str
        :rtype: str
        """
        ret = self.preprocess(s)
        C = 0
        R = 0
        p = list()
        for i in range(len(ret)):
            p.append(0)
        for i in range(1, len(ret) - 1):
            mirror_i = 2 * C - i
            if p[mirror_i] < R - i:
                p[i] = p[mirror_i]
            else:
                p[i] = R - i
                for j in range(p[i] + 1, len(ret)):
                    if ret[i + j] == ret[i - j]:
                        p[i] += 1
                    else:
                        break
                cur_R = i + p[i]
                if cur_R > R:
                    C = i
                    R = cur_R
        center = 0
        max_len = 0
        for i in range(1, len(ret) - 1):
            if p[i] > max_len:
                max_len = p[i]
                center = i
        return s[(center-max_len+1)/2-1 : (center+max_len-1)/2]

if __name__ == '__main__':
    sol = Solution()
    s = "abcbb"
    print sol.longestPalindrome(s)
