
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.strip().split(" ")
        if len(words) != len(pattern):
            return False
        w2p, p2w = dict(), dict()
        for i in xrange(len(pattern)):
            if not p2w.has_key(pattern[i]) and not w2p.has_key(words[i]):
                w2p[words[i]] = pattern[i]
                p2w[pattern[i]] = words[i]
            elif not w2p.has_key(words[i]) or w2p[words[i]] != pattern[i]:
                return False
        return True