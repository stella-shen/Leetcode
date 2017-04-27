
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

        last_profit = nums[0]
        cur_profit = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = cur_profit
            cur_profit = max(last_profit + nums[i], cur_profit)
            last_profit = tmp

        return cur_profit
