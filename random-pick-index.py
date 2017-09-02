import random

class Solution(object):

    def __init__(self, nums):
        """   
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        cnt = 0
        for i in xrange(len(self.nums)):
            if self.nums[i] != target:
                continue
            if cnt == 0 or random.randint(0, cnt) == 0:
                res = i
            cnt += 1
        return res