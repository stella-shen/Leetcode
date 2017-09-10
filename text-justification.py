class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def connect(line, maxWidth, is_last):
            res = ""
            if is_last:
                for word in line:
                    res += word
                    if len(res) < maxWidth:
                        res += " "
                while len(res) < maxWidth:
                    res += " "
            else:
                word_cnt = len(line)
                if word_cnt == 1:
                    space_cnt = maxWidth - len(line[0])
                    res = line[0] + " " * space_cnt
                else:
                    space_cnt = maxWidth
                    for word in line:
                        space_cnt -= len(word)
                    between = space_cnt / (word_cnt - 1)
                    last = space_cnt % (word_cnt - 1)
                    for i in xrange(word_cnt):
                        res += line[i]
                        if i == word_cnt - 1:
                            break
                        elif i < last:
                            res += " " * (between + 1)
                        else:
                            res += " " * between
            return res

        cur_len = 0
        cur_line = list()
        res = list()
        for i in xrange(len(words)):
            word = words[i]
            cur_len += len(word)
            if cur_len <= maxWidth:
                cur_line.append(word)
                cur_len += 1
            else:
                line = connect(cur_line, maxWidth, False)
                res.append(line)
                cur_len = len(word) + 1
                cur_line = [word]
            if i == len(words) - 1:
                line = connect(cur_line, maxWidth, True)
                res.append(line)
        return res

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words_2 = [""]
    print Solution().fullJustify(words_2, 0)
