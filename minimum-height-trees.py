
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        neighbours = collections.defaultdict(set)
        for u, v in edges:
            neighbours[u].add(v)
            neighbours[v].add(u)

        pre_level, unvisited = [], set()
        for i in xrange(n):
            if len(neighbours[i]) == 1:
                pre_level.append(i)
            unvisited.add(i)

        while len(unvisited) > 2:
            cur_level = list()
            for u in pre_level:
                unvisited.remove(u)
                for v in neighbours[u]:
                    if v in unvisited:
                        neighbours[v].remove(u)
                        if len(neighbours[v]) == 1:
                            cur_level.append(v)
            pre_level = cur_level

        return list(unvisited)

