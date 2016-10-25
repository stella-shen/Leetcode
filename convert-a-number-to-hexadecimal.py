
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        if not num:
            return "0"
        while num and len(res) != 8:
            tmp = num & 15
            if tmp < 10:
                res.append(str(chr(ord('0') + tmp)))
            else:
                res.append(str(chr(ord('a') + tmp - 10)))
            num >>= 4
        res.reverse()
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    print sol.toHex(-100000)
    print sol.toHex(0)
