
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        ptr_g = 0
        ptr_s = 0
        while ptr_g < len(g) and ptr_s < len(s):
            if g[ptr_g] <= s[ptr_s]:
                count += 1
                ptr_g += 1
                ptr_s += 1
            else:
                ptr_s += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    g = [1, 2]
    s = [1, 2, 3]
    a = sol.findContentChildren(g, s)
    print a