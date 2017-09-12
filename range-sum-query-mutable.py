class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return 
        self.nums = nums
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        for i in xrange(len(nums)):
            self.add(i + 1, nums[i])

    def lowbit(self, x):
        return x & (-x)

    def add(self, x, val):
        while x <= self.n:
            self.bit[x] += val
            x += self.lowbit(x)

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.bit[x]
            x -= self.lowbit(x)
        return res

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        return self.sum(j + 1) - self.sum(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)