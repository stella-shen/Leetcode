
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        if s == "":
            return 0
        ret = 0
        sign = 1
        flag = False
        if s[0] == '-':
            sign = -1
            flag = True
        elif s[0] == '+':
            sign = 1
            flag = True
        elif ord(s[0]) < ord('0') or ord(s[0]) > ord('9'):
            return 0
        start = 0
        if flag:
            start = 1
        for c in s[start:]:
            if ord(c) < ord('0') or ord(c) > ord('9'):
                break
            ret = ret * 10 + ord(c) - ord('0')
        ret *= sign
        if ret > 2147483647:
            ret = 2147483647
        if ret < -2147483648:
            ret = -2147483648
        return ret

if __name__ == '__main__':
    sol = Solution()
    s = "1"
    print sol.myAtoi(s)
