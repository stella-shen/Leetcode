
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        len1 = len(num1) - 1
        len2 = len(num2) - 1
        carry = 0
        while len1 >= 0 or len2 >= 0 or carry > 0:
            if len1 >= 0:
                carry += ord(num1[len1]) - ord('0')
                len1 -= 1
            if len2 >= 0:
                carry += ord(num2[len2]) - ord('0')
                len2 -= 1
            res.append(str(carry % 10))
            carry /= 10
        res.reverse()
        return "".join(res)

if __name__ == '__main__':
    sol = Solution()
    print sol.addStrings("13", "12")
