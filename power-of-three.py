import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        res = math.log10(n) / math.log10(3)
        return (res - int(res)) == 0
        
if __name__ == '__main__':
    sol = Solution()
    print sol.isPowerOfThree(243)
