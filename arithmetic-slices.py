
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        dp = 0
        for i in xrange(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.numberOfArithmeticSlices([1, 2, 3, 4])    
