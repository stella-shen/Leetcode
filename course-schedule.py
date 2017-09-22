import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree, out_degree = collections.defaultdict(set), collections.defaultdict(set)
        zero_in_degree = collections.deque()

        for i, j in prerequisites:
            in_degree[i].add(j)
            out_degree[j].add(i)

        for i in xrange(numCourses):
            if len(in_degree[i]) == 0:
                zero_in_degree.append(i)

        while zero_in_degree:
            cur_course = zero_in_degree.popleft()

            if len(out_degree[cur_course]) != 0:
                for course in out_degree[cur_course]:
                    in_degree[course].discard(cur_course)
                    if len(in_degree[course]) == 0:
                        zero_in_degree.append(course)
            del out_degree[cur_course]
        
        if len(out_degree) != 0:
            return False
        return True

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print Solution().canFinish(numCourses, prerequisites)
