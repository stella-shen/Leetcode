
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = list()
        while n != 1 and n not in lookup:
            if n not in lookup:
                lookup.append(n)
            digits = self.depart(n)
            n = 0
            for d in digits:
                n += d ** 2
        return n == 1
            

    def depart(self, n):
        digits = list()
        while n > 0:
            digits.append(n % 10)
            n /= 10
        return digits

if __name__ == '__main__':
    sol = Solution()
    print sol.isHappy(29)
