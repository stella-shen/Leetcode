
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        last_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_len = i - last_zero - 1
                last_zero = i
                if cur_len > max_len:
                    max_len = cur_len
            elif i == len(nums) - 1:
                cur_len = i - last_zero
                if cur_len > max_len:
                    max_len = cur_len
        return max_len

