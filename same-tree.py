
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        else:
            if p == None or q == None:
                return False
            else:
                if p.val == q.val:
                    l = self.isSameTree(p.left, q.left)
                    r = self.isSameTree(p.right, q.right)
                    return l and r
                else:
                    return False

if __name__ == '__main__':
    sol = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print sol.isSameTree(root1, root2)
