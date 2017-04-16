# -*- coding: utf-8 -*-
import sys

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import numpy as np
        if len(points) <= 2:
            return len(points)

        max_p = 0
        for i in range(len(points)):
            curk_dict = dict()
            k = sys.maxint
            x1 = points[i].x
            y1 = points[i].y
            same = 0
            for j in range(i + 1, len(points)):
                x2 = points[j].x
                y2 = points[j].y
                if x1 == x2 and y1 == y2:
                    same += 1
                    continue
                elif x1 == x2 and y1 != y2:
                    k = sys.maxint
                    b = 0
                else:
                    k = np.longdouble(y1-y2) / np.longdouble(x1-x2)
                    b = y1 - k * x1
                    print b
                if curk_dict.get((k, b)) is None:
                    curk_dict[(k, b)] = 2
                else:
                    curk_dict[(k, b)] += 1

            if curk_dict.keys():
                for key in curk_dict.keys():
                    if max_p < curk_dict[key] + same:
                        max_p = curk_dict[key] + same
            else:
                if max_p < same + 1:
                    max_p = same + 1            

        return max_p

if __name__ == '__main__':
    sol = Solution()
    input = [[0,0],[94911151,94911150],[94911152,94911151]]
    points = list()
    for i in input:
        points.append(Point(i[0], i[1]))
    print sol.maxPoints(points)
