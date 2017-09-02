import random

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if self.head is None:
            return
        res_node = self.head
        cur_node = self.head
        cnt = 1
        while cur_node != None:
            if random.randint(1, cnt) == 1:
                res_node = cur_node
            cnt += 1
            cur_node = cur_node.next
        return res_node.val
