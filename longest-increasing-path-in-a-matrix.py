
class Solution(object):
    def dfs(self, x, y, matrix, dp):
        if dp[x][y] != 0:
            return dp[x][y]
        dises = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(matrix)
        column = len(matrix[0])
        max_dis = 1
        for dis in dises:
            next_x = x + dis[0]
            next_y = y + dis[1]
            if 0 <= next_x < row and 0 <= next_y < column:
                if matrix[next_x][next_y] > matrix[x][y]:
                    max_dis = max(max_dis, self.dfs(next_x, next_y, matrix, dp) + 1)
        dp[x][y] = max_dis
        return dp[x][y]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        row = len(matrix)
        column = len(matrix[0])
        dp = [[0 for _ in xrange(column)] for _ in xrange(row)]
        for i in xrange(row):
            for j in xrange(column):
                self.dfs(i, j, matrix, dp)
        return max([max(x) for x in dp])

if __name__ == '__main__':
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print Solution().longestIncreasingPath(matrix)
