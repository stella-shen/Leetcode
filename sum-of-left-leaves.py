
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = 0
        if root.left == None:
            return res + self.sumOfLeftLeaves(root.right)
        if root.left.left == None and root.left.right == None:
            res += root.left.val
        res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    rightlc = TreeNode(4)
    rightrc = TreeNode(5)
    root.left = left
    root.right = right
    left.left = rightlc
    left.right = rightrc
    print sol.sumOfLeftLeaves(root)
