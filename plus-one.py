
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        
        for i in reversed(range(len(digits))):
            temp = carry
            carry = (digits[i]+carry)/10
            digits[i] = (digits[i]+temp)%10

        if carry == 1:
            digits.instert(0, carry)

        return digits
