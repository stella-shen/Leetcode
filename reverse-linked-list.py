
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = None
        while head != None:
            suc = head.next
            head.next = cur
            cur = head
            head = suc
        return cur

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    print sol.reverseList(head).val
