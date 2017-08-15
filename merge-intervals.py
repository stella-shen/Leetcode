
class Interval(object):
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals
        ret = list()
        intervals.sort(key=lambda x: x.start)
        ret.append(intervals[0])
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= ret[-1].end:
                if intervals[i].end > ret[-1].end:
                    ret[-1].end = intervals[i].end
            else:
                ret.append(intervals[i])
        return ret

if __name__ == '__main__':
    i1 = Interval(1, 3)
    i2 = Interval(2, 6)
    i3 = Interval(8, 10)
    i4 = Interval(15, 18)
    l = [i1, i2, i3, i4]
    ret = Solution().merge(l)
    for r in ret:
        print r.start, r.end
