
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        ret = [0 for i in range(num + 1)]
        ret[1] = 1
        power_num = 1

        for ind in range(2, num + 1):
            if ind == (2 ** power_num):
                ret[ind] = 1
                power_num += 1
            else:
                ret[ind] = 1 + ret[ind - (2 ** (power_num - 1))]

        return ret
        
if __name__ == '__main__':
    sol = Solution()
    print sol.countBits(5)
