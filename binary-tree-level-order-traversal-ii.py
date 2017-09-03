import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        cur_level = [root]
        children_level = []
        while cur_level:
            cur_vals = list()
            for node in cur_level:
                cur_vals.append(node.val)
                if node.left is not None:
                    children_level.append(node.left)
                if node.right is not None:
                    children_level.append(node.right)
            res.append(cur_vals)
            cur_level = children_level
            children_level = []
        return res[: :-1]