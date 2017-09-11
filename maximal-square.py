class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row, column = len(matrix), len(matrix[0])
        dp = [[0 for j in xrange(column)] for i in xrange(row)]

        max_size = 0
        for i in xrange(column):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                max_size = 1
        for i in xrange(row):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                max_size = 1
        
                
        for i in xrange(1, row):
            for j in xrange(1, column):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    max_size = max(dp[i][j], max_size)
        return max_size * max_size