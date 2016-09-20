
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = list()
        ret = True
        for i in range(0, 26):
            count.append(0)
        for c in magazine:
            count[ord(c) - ord('a')] += 1
        for c in ransomNote:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                ret = False
                break
        return ret

if __name__ == '__main__':
    sol = Solution()
    ransom = "aa"
    magazine = "ab"
    print sol.canConstruct(ransom, magazine)
