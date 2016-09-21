
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = list()
        for i in xrange(26):
            count.append(0)
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        for i in xrange(26):
            if count[i] != 0:
                return False
        return True

if __name__ == '__main__':
    s = "ac"
    t = "bb"
    sol = Solution()
    print sol.isAnagram(s, t)
