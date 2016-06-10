
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        ans = ret
        carry = 0
        while(l1 != None and l2 != None):
            tmp = l1.val + l2.val + carry
            ret.next = ListNode(tmp % 10)
            l1 = l1.next
            l2 = l2.next
            carry = tmp / 10
            ret = ret.next
        while(l1 != None):
            tmp = l1.val + carry
            ret.next = ListNode(tmp % 10)
            l1 = l1.next
            carry = tmp / 10
            ret = ret.next
        while(l2 != None):
            tmp = l2.val + carry
            ret.next = ListNode(tmp % 10)
            l2 = l2.next
            carry = tmp / 10
            ret = ret.next
        if carry != 0:
            ret.next = ListNode(carry)
            ret = ret.next
        return ans.next

l1 = ListNode(5)
l2 = ListNode(5)
sol = Solution()
ret = sol.addTwoNumbers(l1, l2)
while(ret != None):
    print ret.val
    ret = ret.next

