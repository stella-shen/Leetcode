#the shortest way solution

class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        preMap = dict()
        if beginWord not in wordList:
            wordList.add(beginWord)
        length = len(beginWord)
        result = list()
        cur_level = set()
        cur_level.add(beginWord)
        for word in wordList:
            preMap[word] = list()

        def buildPath(path, word):
            if len(preMap[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0, word)
            for w in preMap[word]:
                buildPath(path, w)
            path.pop(0)
        
        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level:
                wordList.remove(word)
            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i+1:]
                    for j in range(ord('a'), ord('z')+1):
                        if word[i] != chr(j):
                            neighbour = left + chr(j) + right
                            if neighbour in wordList:
                                preMap[neighbour].append(word)
                                cur_level.add(neighbour)
            if len(cur_level) == 0:
                return []
            if endWord in cur_level:
                break
        buildPath([], endWord)
        return result

if __name__ == '__main__':
    sol = Solution()
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot","dot","dog"]
    print sol.findLadders(beginWord, endWord, wordList)
