# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root

if __name__ == '__main__':
    #initiation
    root = TreeNode(4)
    lc = TreeNode(2)
    llc = TreeNode(1)
    lrc = TreeNode(3)
    rc = TreeNode(7)
    rlc = TreeNode(6)
    rrc = TreeNode(9)
    lc.left = llc
    lc.right = lrc
    rc.left = rlc
    rc.right = rrc
    root.left = lc
    root.right = rc
    print root.left.val
    sol = Solution()
    sol.invertTree(root)
    print root.left.val
