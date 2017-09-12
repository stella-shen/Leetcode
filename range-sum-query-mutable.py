class NumArray(object):

    class SegmentTreeNode:
        def __init__(self, i, j, s):
            self.start, self.end, self.sum = i, j, s

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        def buildHelper(nums, start, end):
            if start > end:
                return None
            root = self.SegmentTreeNode(start, end, 0)

            if start == end:
                root.sum = nums[start]
                return root

            root.left = buildHelper(nums, start, (start + end) / 2)
            root.right = buildHelper(nums, (start + end) / 2 + 1, end)

            root.sum = 0
            if root.left:
                root.sum += root.left.sum
            if root.right:
                root.sum += root.right.sum
            return root
        self.root = buildHelper(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def updateHelper(root, i, val):
            if not root or root.start > i or root.end < i:
                return
            if root.start == i and root.end == i:
                root.sum = val
                return
            updateHelper(root.left, i, val)
            updateHelper(root.right, i, val)

            root.sum = 0
            if root.left:
                root.sum += root.left.sum
            if root.right:
                root.sum += root.right.sum
        
        if self.nums[i] != val:
            self.nums[i] = val
            updateHelper(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumRangeHelper(root, start, end):
            if not root or root.end < start or root.start > end:
                return 0
            if root.start >= start and root.end <= end:
                return root.sum
            return sumRangeHelper(root.left, start, end) + \
                   sumRangeHelper(root.right, start, end)
        return sumRangeHelper(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)