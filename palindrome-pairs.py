
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        lookup = dict()
        ans = list()
        for i, word in enumerate(words):
            lookup[word] = i

        for i in xrange(len(words)):
            for j in xrange(len(words[i]) + 1):
                right = words[i][j:]
                left = words[i][:j]
                if j > 0 and is_palindrome(left) and right[::-1] in lookup and lookup[right[::-1]] != i:
                    ans.append([lookup[right[::-1]], i])
                if is_palindrome(right) and left[::-1] in lookup and lookup[left[::-1]] != i:
                    ans.append([i, lookup[left[::-1]]])
        return ans

if __name__ == '__main__':
    words = ["a", ""]
    print Solution().palindromePairs(words)
