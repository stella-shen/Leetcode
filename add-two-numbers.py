
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
        while(l1 != None and l2 != None):
            tmp = l1.val + l2.val
            ret.val += tmp % 10
            l1 = l1.next
            l2 = l2.next
            ret.next = ListNode(tmp / 10)
            ret = ret.next
        while(l1 != None):
            ret.val += l1.val % 10
            ret.next = ListNode(l1.val / 10)
            l1 = l1.next
            ret = ret.next
        while(l2 != None):
            ret.val += l2.val % 10
            ret.next = ListNode(l2.val / 10)
            l2 = l2.next
            ret = ret.next
        if ret.val == 0:
            ret = None
        return ans

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
sol = Solution()
ret = sol.addTwoNumbers(l1, l2)
while(ret != None):
    print ret.val
    ret = ret.next

