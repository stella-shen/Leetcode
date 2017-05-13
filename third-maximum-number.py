
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cp_nums = set(nums)
        if len(cp_nums) < 3:
            return max(cp_nums)

        max_nums = [float('-inf'), float('-inf'), float('-inf')]
        for num in cp_nums:
            if num > max_nums[0]:
                max_nums[0], max_nums[1], max_nums[2] = num, max_nums[0], max_nums[1]
            elif num > max_nums[1]:
                max_nums[1], max_nums[2] = num, max_nums[1]
            elif num > max_nums[2]:
                max_nums[2] = num

        return max_nums[2]

