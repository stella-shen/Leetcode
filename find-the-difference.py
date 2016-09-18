
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = list()
        for i in range(0, 26):
            counter.append(0)
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for c in t:
            counter[ord(c) - ord('a')] -= 1
        for i in range(0, 26):
            if counter[i] != 0:
                return chr(i + ord('a'))

if __name__ == '__main__':
    sol = Solution()
    print sol.findTheDifference('adc', 'dcab')
