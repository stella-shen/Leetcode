
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None

        s1 = self.sortList(head)
        s2 = self.sortList(slow)

        def merge(s1, s2):
            dummy = ListNode(0)
            prev = dummy

            while s1 != None and s2 != None:
                if s1.val <= s2.val:
                    prev.next = s1
                    prev = s1
                    s1 = s1.next
                else:
                    prev.next = s2
                    prev = s2
                    s2 = s2.next
            if s1 != None:
                prev.next = s1
            if s2 != None:
                prev.next = s2

            return dummy.next
        return merge(s1, s2)
