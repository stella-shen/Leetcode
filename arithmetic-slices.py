
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        for start in xrange(len(A) - 2):
            d = A[start + 1] - A[start]
            for end in xrange(start+2, len(A)):
                if A[end] - A[end - 1] == d:
                    res += 1
                else:
                    break
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.numberOfArithmeticSlices([1, 2, 3, 4])    
