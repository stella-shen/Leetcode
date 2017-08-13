
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def calculate(a, b):
            if a == b:
                return a
            for i in xrange(len(a)):
                if ord(a[i]) > ord(b[i]):
                    return b
                elif ord(a[i]) < ord(b[i]):
                    return a
        max_len = 0
        sorted_list = sorted(d, key = lambda x: len(x), reverse = True)
        res = list()
        for word in sorted_list:
            if len(word) < max_len:
                break
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
                if i == len(word) and i >= max_len:
                    max_len = i
                    res.append(word)
                    break
        if len(res) == 0:
            return ""
        min_word = res[0]
        for i in xrange(1, len(res)):
            min_word = calculate(min_word, res[i])
        return min_word

if __name__ == '__main__':
    print Solution().findLongestWord("abpcplea", ["aaaaa", "apple", "monkey", "plea"])
