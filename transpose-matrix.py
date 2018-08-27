class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = list()
        for i in xrange(len(A[0])):
            cur_list = list()
            for j in xrange(len(A)):
                cur_list.append(A[j][i])
            result.append(cur_list)
        return result

if __name__ == "__main__":
    sol = Solution()
    A = [[1,2,3],[4,5,6],[7,8,9]]
    print sol.transpose(A)