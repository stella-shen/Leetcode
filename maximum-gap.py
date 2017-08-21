
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        max_gap = 0
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i - 1] > max_gap:
                max_gap = nums[i] - nums[i - 1]
        return max_gap

if __name__ == '__main__':
    print Solution().maximumGap([1, 1000000])
