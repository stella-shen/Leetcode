#Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        if len(points) < 3:
            return points
        def orientation(p, q, r):
            #p, q is the points in the stack, r is the next
            return (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
        
        points.sort(key = lambda p: (p.x, p.y))
        stack = list()
        for point in points:
            while len(stack) > 1 and orientation(stack[-2], stack[-1], point) > 0:
                stack.pop()
            stack.append(point)
        for i in reversed(xrange(len(points))):
            while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) > 0:
                stack.pop()
            stack.append(points[i])
        return list(set(stack))

if __name__ == '__main__':
    points = [Point(1, 1), Point(2, 2), Point(2, 0), Point(2, 4), Point(3, 3), Point(4, 2)]
    res = Solution().outerTrees(points)
    for r in res:
        print r.x, r.y