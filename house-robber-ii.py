class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robRange(nums, 0, len(nums) - 1), \
                    self.robRange(nums, 1, len(nums)))


    def robRange(self, nums, start, end):
        num_i = nums[start]
        cur = 0
        for i in xrange(start + 1, end):
            cur, temp = num_i, cur
            num_i = max(nums[i] + temp, cur)
        return num_i