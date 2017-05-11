
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        cur = 0
        for i in xrange(len(nums)):
            if nums[i] != nums[cur]:
                nums[i], nums[cur+1] = nums[cur+1], nums[i]
                cur += 1

        return cur + 1 
        