
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        ret = [[1]]
        if numRows == 1:
            return ret
        
        for i in range(2, numRows + 1):
            cur = list()
            for j in range(i):
                if j == 0 or j == i-1:
                    cur.append(1)
                else:
                    cur.append(ret[i-2][j-1] + ret[i-2][j])
            ret.append(cur)

        return ret

if __name__ == '__main__':
    sol = Solution()
    print sol.generate(4)
