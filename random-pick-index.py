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
        res = list()
        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                res.append(i)
        return random.choice(res)