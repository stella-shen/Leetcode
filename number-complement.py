
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        ret = 0
        MASK = 0x00000001
        while num > 0:
            cur = 1 - (num & MASK)
            cur <<= cnt
            ret += cur
            cnt += 1
            num >>= 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    print sol.findComplement(13)
