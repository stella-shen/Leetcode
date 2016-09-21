
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def count_bit(bits):
            count = 0
            while bits:
                bits &= bits - 1
                count += 1
            return count
        ret = list()
        for h in xrange(12):
            for m in xrange(60):
                if count_bit(h) + count_bit(m) == num:
                    ret.append('%d:%02d' % (h, m))
        return ret

if __name__ == '__main__':
    sol = Solution()
    num = 1
    print sol.readBinaryWatch(num)
