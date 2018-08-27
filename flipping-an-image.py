class Solution(object):
    def flipAndInvertOneRow(self, row):
        for i in xrange((len(row) + 1) // 2):
            row[i], row[len(row)-1-i] = 1 - row[len(row)-1-i], 1 - row[i]

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            self.flipAndInvertOneRow(row)
        return A


if __name__ == "__main__":
    sol = Solution()
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print sol.flipAndInvertImage(A)
