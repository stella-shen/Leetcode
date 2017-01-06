import operator

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        count = 0
        neighbour = 0
        line = len(grid)
        row = len(grid[0])
        for i in range(0, line):
            for j in range(0, row):
                if grid[i][j] == 1:
                    count += 1
                    if (i + 1 < line) and grid[i + 1][j] == 1:
                        neighbour += 1
                    if (j + 1 < row) and grid[i][j + 1] == 1:
                        neighbour += 1
        return count * 4 - neighbour * 2
        """
        ret = 0
        for row in grid + map(list, zip(*grid)):
            ret +=  sum(map(operator.ne, [0] + row, row + [0]))
        return ret



if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print sol.islandPerimeter(grid)
        