
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10

        while x >= 10:
            right = x % 10
            left = x / div
            if right != left:
                return False
            x %= div
            x /= 10
            div /= 100

        return True
        