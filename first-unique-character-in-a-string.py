
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = list()
        for i in xrange(26):
            count.append(0)
        for c in s:
            count[ord(c) - ord('a')] += 1
        for i in xrange(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                flag = False
                return i
        return -1
        
if __name__ == '__main__':
    sol = Solution()
    s = "loveleetcode"
    print sol.firstUniqChar(s)

