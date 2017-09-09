
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.existHelper(board, word, 0, i, j, visited):
                    return True
        return False

    def existHelper(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
           or visited[i][j] or board[i][j] != word[cur]:
           return False

        visited[i][j] = True
        
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for  delta in deltas:
            next_i = i + delta[0]
            next_j = j + delta[1]
            if self.existHelper(board, word, cur + 1, next_i, next_j, visited):
                return True
        visited[i][j] = False

        return False

