import random

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        median = (len(nums) - 1) // 2
        nums[: : 2], nums[1: :2] = nums[median: : -1], nums[: median: -1]
