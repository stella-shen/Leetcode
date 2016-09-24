
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if s == "":
            return 0
        index = len(s) - 2
        ret = roman[s[-1]]
        while index >= 0:
            if roman[s[index]] < roman[s[index + 1]]:
                ret -= roman[s[index]]
            else:
                ret += roman[s[index]]
            index -= 1
        return ret


if __name__ == '__main__':
    sol = Solution()
    s = "XI"
    print sol.romanToInt(s)
