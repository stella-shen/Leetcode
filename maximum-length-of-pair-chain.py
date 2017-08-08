
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        cnt = 0
        i = 0
        for j in xrange(len(pairs)):
            if j == 0 or pairs[j][0] > pairs[i][1]:
                cnt += 1
                i = j
        return cnt


if __name__ == '__main__':
    sol = Solution()
    print sol.findLongestChain([[1,2], [2,3], [3,4]])
