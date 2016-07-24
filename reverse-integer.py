import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        flag = False
        if x < 0:
            x *= -1
            flag = True

        while x > 0:
            ret = ret * 10 + x % 10
            x /= 10

        if ret > 2147483647:    #Here using sys.maxint will not pass...
            return 0

        if flag:
            ret *= -1
        return ret

if __name__ == '__main__':
    sol = Solution()
    x = 1534236469
    print sol.reverse(x)
