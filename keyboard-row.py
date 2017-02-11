
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = list()
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        for word_raw in words:
            flag = True
            word = word_raw.lower()
            for i in range(1, len(word)):
                if word[i - 1] in row1 and word[i] not in row1:
                    flag = False
                    break
                elif word[i - 1] in row2 and word[i] not in row2:
                    flag = False
                    break
                elif word[i - 1] in row3 and word[i] not in row3:
                    flag = False
                    break
            if flag:
                ret.append(word_raw)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print sol.findWords(["Hello", "Alaska", "Dad", "Peace"])
