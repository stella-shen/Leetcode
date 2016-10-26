#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        cur = head.next
        prev = head
        while cur != None:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                if prev.next != None:
                    cur = prev.next
                else:
                    break
        return head

if __name__ == '__main__':
    head = ListNode(1)
    two = ListNode(1)
    three = ListNode(2)
    head.next = two
    two.next = three
    sol = Solution()
    sol.deleteDuplicates(head)
    print head.val, head.next.val, head.next.next.val
