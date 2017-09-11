# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robHelper(root):
            if not root:
                return (0, 0)
            left, right = robHelper(root.left), robHelper(root.right)
            return (root.val + left[1] + right[1], max(left) + max(right))
        return max(robHelper(root))

if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    left.right = TreeNode(3)
    right.left = TreeNode(1)
    print Solution().rob(root)