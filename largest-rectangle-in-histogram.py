
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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