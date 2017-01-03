
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = x ^ y
        ret = 0
        while result > 0:
            if result & 1 == 1:
                ret += 1
            result >>= 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    print sol.hammingDistance(1, 4)
