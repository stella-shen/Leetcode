class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
            increasing, area, i = list(), 0, 0
            while i <= len(heights):
                if not increasing or (i < len(heights) and heights[i] > heights[increasing[-1]]):
                    increasing.append(i)
                    i += 1
                else:
                    last = increasing.pop()
                    if not increasing:
                        area = max(area, heights[last] * i)
                    else:
                        area = max(area, heights[last] * (i - increasing[-1] - 1))
            return area 

        if not matrix:
            return 0

        res = 0
        heights = [0] * len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] = heights[j] + 1
                else:
                    heights[j] = 0
            res = max(res, largestRectangleArea(heights))
        return res