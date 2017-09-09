
class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, cur):
        if start == len(word):
            return cur.is_string
        if word[start] in cur.leaves:
            return self.searchHelper(word, start + 1, cur.leaves[word[start]])
        elif word[start] == '.':
            for l in cur.leaves:
                if self.searchHelper(word, start + 1, cur.leaves[l]):
                    return True
        return False