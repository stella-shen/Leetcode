class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = list()
        for i in range(len(nums)):
          menos = target - nums[i]
          for j in range(i + 1, len(nums)):
            if nums[j] == menos:
              ret.append(i)
              ret.append(j)
        return ret