#Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            tmp = node.next
            node.val = tmp.val
            node.next = tmp.next
            del tmp

if __name__ == '__main__':
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    first.next = second
    second.next = third
    third.next = fourth
    sol = Solution()
    sol.deleteNode(third)
    print second.next.val
