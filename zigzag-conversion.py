
class Solution(object):
    def convert(self, s, numRows):
        """

        :type s: str
        :type numRows: int
        :rtype:str
        """
        if numRows <= 1:
            return s
        if s == "":
            return s
        ret = ""
        loop_size = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), loop_size):
                ret += s[j]
                if i != 0 and i != numRows - 1:
                    temp = j + loop_size - 2 * i
                    if temp < len(s):
                        ret += s[temp]
        return ret

if __name__ == '__main__':
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 4
    print sol.convert(s, numRows)
